from numpy.core.records import array

from ocr_attribute_extraction import document
from .attribute_name import Colors, Part, attribute_keyword_lookup, upper_body_part_to_color, lower_body_part_to_color, AttributeName

import stanza
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import numpy as np
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
stanza.download('en')
stanza_pipeline = stanza.Pipeline('en')


class AdvancedAttributeExtractionStage:
    def process(self, document):
        text = document.text

        # Splitting the text into sentences
        sentences = nltk.sent_tokenize(text.lower())

        fcluster = []
        total_feature_list = []
        final_cluster = []
        dic = {}

        pronouns = []

        for sentence in sentences:
            word_list = nltk.word_tokenize(sentence)  # Splitting up into words

            # Part-of-Speech Tagging to each word
            tagged_words = nltk.pos_tag(word_list)

            # Use stanza to find word dependencies
            doc = stanza_pipeline(sentence)
            dep_node = []
            for dep_edge in doc.sentences[0].dependencies:
                dep_node.append(
                    [dep_edge[2].text, dep_edge[0].id, dep_edge[1]])
            for i in range(len(dep_node)):
                if (int(dep_node[i][1]) != 0):
                    dep_node[i][1] = word_list[(int(dep_node[i][1]) - 1)]

            featureList = []
            categories = []
            for word in tagged_words:
                if (word[1] in ['NN', 'PRP', 'PRP$']):
                    pronouns.append(word)
                if (word[1] in ['JJ', 'NN', 'NNS']):
                    featureList.append(word)
                    # This list will store all the features for every sentence
                    total_feature_list.append(list(word))
                    categories.append(word[0])

            for word in featureList:
                filist = []
                for j in dep_node:
                    if ((j[0] == word[0] or j[1] == word[0]) and j[2] in ["amod", "nsubj"]):
                        if (j[0] == word[0]):
                            filist.append(j[1])
                        else:
                            filist.append(j[0])
                fcluster.append([word[0], filist])

        for word in total_feature_list:
            dic[word[0]] = word[1]

        for word in fcluster:
            if (dic[word[0]] == "NN" or dic[word[0]] == "NNS"):
                if (word not in final_cluster):
                    final_cluster.append(word)

        for name in AttributeName:
            document.attributes[name] = -1

        document.attributes[AttributeName.Gender_Female] = is_female(pronouns)
        parse_attributes(final_cluster, document)

        return [document]


def is_female(pronoun_list: array):
    indicate_male = 0
    indicate_female = 0
    for pronoun in pronoun_list:
        if pronoun[0] in attribute_keyword_lookup["Gender_Male"]:
            indicate_male += 1
        if pronoun[0] in attribute_keyword_lookup["Gender_Female"]:
            indicate_female += 1
        if indicate_female + indicate_male > 0:
            return int(indicate_female > indicate_male)
        return -1


def parse_attributes(dep_list: array, document: document.Document):
    for word in dep_list:
        print(word)
        parse_body_part(word, Part.UpperBody, document)
        parse_body_part(word, Part.LowerBody, document)
        if word[0] in attribute_keyword_lookup[Part.Backpack.value]:
            document.attributes[AttributeName.Accessory_Backpack] = 1


def parse_body_part(word, part: Part, document: document.Document):
    attribute_keyword_lookup
    object_word = word[0]
    attributes = word[1]
    if part == Part.UpperBody:
        part_to_color = upper_body_part_to_color
        attribute_short = AttributeName.UpperBody_Length_Short
        attribute_color_mixture = AttributeName.UpperBody_Color_Mixture
    elif part == Part.LowerBody:
        part_to_color = lower_body_part_to_color
        attribute_short = AttributeName.LowerBody_Length_Short
        attribute_color_mixture = AttributeName.LowerBody_Color_Mixture
    else:
        return

    # Does the clothing already imply length?
    if object_word in attribute_keyword_lookup["Length_Short"]:
        document.attributes[attribute_short] = 1
    if object_word in attribute_keyword_lookup["Length_Long"]:
        document.attributes[attribute_short] = 0

    # Do the word dependencies imply color or length?
    if object_word in attribute_keyword_lookup[part.value]:
        colors_found = 0
        for attribute in attributes:
            for part, color in part_to_color.items():
                if attribute in attribute_keyword_lookup[color.value]:
                    colors_found += 1
                    document.attributes[part] = 1
            if attribute in attribute_keyword_lookup["Length_Short"]:
                document.attributes[attribute_short] = 1
            elif attribute in attribute_keyword_lookup["Length_Long"]:
                document.attributes[attribute_short] = 0
        if colors_found > 1:
            document.attributes[attribute_color_mixture] = 1

from .document import Document
from .stage import Stage
from .attribute_name import Colors, Part, attribute_keyword_lookup, upper_body_part_to_color, lower_body_part_to_color, AttributeName

import stanza


class AdvancedAttributeExtractionStage(Stage):
    def __init__(self, language, download_models):
        Stage.__init__(self)
        self.keyword_lookup = attribute_keyword_lookup[language]

        if download_models:
            stanza.download(language)

        self.stanza_pipeline = stanza.Pipeline(
            # Language specific model
            lang=language,
            # multi-word-token expansion, part-of-speech tags, lemmatization, dependency parsing
            # Comparing lemma with keywords might give better results
            processors='tokenize,mwt,pos,lemma,depparse'
        )

    def process(self, document):
        gender_indicator_male = 0
        gender_indicator_female = 0
        colors_found = {
            Part.UpperBody.value: 0,
            Part.LowerBody.value: 0,
        }

        # Run stanza pipeline on document text
        doc = self.stanza_pipeline(document.text)

        for sentence in doc.sentences:
            for dependency_node in sentence.dependencies:
                if dependency_node[1] in ['amod', 'nsubj']:
                    # Does one of the two words indicate body part? If so, check the dependency for attributes
                    if self.isBodyPart(dependency_node[0], Part.UpperBody):
                        self.parseDependency(dependency_node[0],
                                             dependency_node[2], Part.UpperBody, document, colors_found)
                    elif self.isBodyPart(dependency_node[0], Part.LowerBody):
                        self.parseDependency(dependency_node[0],
                                             dependency_node[2], Part.LowerBody, document, colors_found)
                    elif self.isBodyPart(dependency_node[2], Part.UpperBody):
                        self.parseDependency(dependency_node[2],
                                             dependency_node[0], Part.UpperBody, document, colors_found)
                    elif self.isBodyPart(dependency_node[2], Part.LowerBody):
                        self.parseDependency(dependency_node[2],
                                             dependency_node[0], Part.LowerBody, document, colors_found)

            for word in sentence.words:
                if word.upos in ['NOUN']:
                    # Does word indicate backpack?
                    if word.text.lower() in self.keyword_lookup[Part.Backpack.value]:
                        document.attributes[AttributeName.Accessory_Backpack.value] = 1

                    # Does word indicate person gender?
                    if self.isWordContained(word, self.keyword_lookup['Gender_Female']):
                        gender_indicator_female += 1
                    elif self.isWordContained(word, self.keyword_lookup['Gender_Male']):
                        gender_indicator_male += 1

                # Parse gender attributed to persons
                if word.upos in ['PRON', 'DET', 'AUX']:
                    if 'Person' in word.feats:
                        if 'Gender=Masc' in word.feats:
                            gender_indicator_male += 1
                        elif 'Gender=Fem' in word.feats:
                            gender_indicator_female += 1

        if gender_indicator_female > gender_indicator_male:
            document.attributes[AttributeName.Gender_Female.value] = 1
        elif gender_indicator_male > gender_indicator_female:
            document.attributes[AttributeName.Gender_Female.value] = 0

        if colors_found[Part.UpperBody.value] > 1:
            document.attributes[AttributeName.UpperBody_Color_Mixture] = 1
        if colors_found[Part.LowerBody.value] > 1:
            document.attributes[AttributeName.LowerBody_Color_Mixture] = 1

        return [document]

    def isBodyPart(self, word, part: Part):
        return self.isWordContained(word, self.keyword_lookup[part.value])

    def isWordContained(self, word, lookup):
        return word.text.lower() in lookup or word.lemma.lower() in lookup

    # Extract length and color if possible
    def parseDependency(self, word, dependency, part: Part, document: Document, colors_found: dict):
        if part == Part.UpperBody:
            part_to_color = upper_body_part_to_color
            attribute_short = AttributeName.UpperBody_Length_Short
        elif part == Part.LowerBody:
            part_to_color = lower_body_part_to_color
            attribute_short = AttributeName.LowerBody_Length_Short

        # Does the word itself already imply length?
        if self.isWordContained(word, self.keyword_lookup["Length_Short"]):
            document.attributes[attribute_short.value] = 1
        if self.isWordContained(word, self.keyword_lookup["Length_Long"]):
            document.attributes[attribute_short.value] = 0

        # Do the word dependencies imply color or length?
        if self.isWordContained(dependency, self.keyword_lookup["Length_Short"]):
            document.attributes[attribute_short.value] = 1
        if self.isWordContained(dependency, self.keyword_lookup["Length_Long"]):
            document.attributes[attribute_short.value] = 0
        for colored_part, color in part_to_color.items():
            if self.isWordContained(dependency, self.keyword_lookup[color.value]):
                colors_found[part.value] += 1
                document.attributes[colored_part.value] = 1

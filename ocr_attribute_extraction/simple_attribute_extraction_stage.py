from .stage import Stage
from .attribute_name import AttributeName, Colors, attribute_keyword_lookup, Part


class SimpleAttributeExtractor:
    def __init__(self, document, attribute_name, word_sequence, match_value=1):
        self.document = document
        self.attribute_name = attribute_name
        self.word_sequence = word_sequence
        self.match_value = match_value
        self.words_matched = 0

    def process_word(self, word):
        if len(self.word_sequence) > 0 and word in self.word_sequence[self.words_matched]:
            self.words_matched += 1

            if self.words_matched == len(self.word_sequence):
                self.document.attributes[self.attribute_name.value] = self.match_value
                self.words_matched = 0
        elif len(self.word_sequence) > 0 and word in self.word_sequence[0]:
            self.words_matched = 1

            if self.words_matched == len(self.word_sequence):
                self.document.attributes[self.attribute_name.value] = self.match_value
                self.words_matched = 0
        else:
            self.words_matched = 0


class SimpleAttributeExtractionStage(Stage):
    def __init__(self, language):
        Stage.__init__(self)
        self.language = language
        self.keyword_lookup = attribute_keyword_lookup[language]

    def process(self, document):
        text_lower = document.text.lower()
        words = text_lower.split()
        extractors = self.init_attribute_extractors(document)

        for word in words:
            word_without_punctuation = word.replace(".", "").replace(",", "")
            for extractor in extractors:
                extractor.process_word(word_without_punctuation)

        return [document]

    def init_attribute_extractors(self, document):
        return [
            # gender
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.Gender_Female,
                word_sequence=[self.keyword_lookup["Gender_Female"]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.Gender_Female,
                word_sequence=[self.keyword_lookup["Gender_Male"]],
                match_value=0
            ),
            # top length
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Length_Short,
                word_sequence=[["shirt", "t-shirt"]]
            ),
            # top color
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Black,
                word_sequence=[self.keyword_lookup[Colors.Black.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Blue,
                word_sequence=[self.keyword_lookup[Colors.Blue.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Brown,
                word_sequence=[self.keyword_lookup[Colors.Brown.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Green,
                word_sequence=[self.keyword_lookup[Colors.Green.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Grey,
                word_sequence=[self.keyword_lookup[Colors.Grey.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Orange,
                word_sequence=[self.keyword_lookup[Colors.Orange.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Pink,
                word_sequence=[self.keyword_lookup[Colors.Pink.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Purple,
                word_sequence=[self.keyword_lookup[Colors.Purple.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Red,
                word_sequence=[self.keyword_lookup[Colors.Red.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_White,
                word_sequence=[self.keyword_lookup[Colors.White.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Yellow,
                word_sequence=[self.keyword_lookup[Colors.Yellow.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Mixture,
                word_sequence=[self.keyword_lookup[Colors.Mixture.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Other,
                word_sequence=[self.keyword_lookup[Colors.Other.value],
                               self.keyword_lookup[Part.UpperBody.value]]
            ),
            # pants length
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Length_Short,
                word_sequence=[["shorts"]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Length_Short,
                word_sequence=[["short"],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            # pants color
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Black,
                word_sequence=[self.keyword_lookup[Colors.Black.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Blue,
                word_sequence=[self.keyword_lookup[Colors.Blue.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Brown,
                word_sequence=[self.keyword_lookup[Colors.Brown.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Green,
                word_sequence=[self.keyword_lookup[Colors.Green.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Grey,
                word_sequence=[self.keyword_lookup[Colors.Grey.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Orange,
                word_sequence=[self.keyword_lookup[Colors.Orange.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Pink,
                word_sequence=[self.keyword_lookup[Colors.Pink.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Purple,
                word_sequence=[self.keyword_lookup[Colors.Purple.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Red,
                word_sequence=[self.keyword_lookup[Colors.Red.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_White,
                word_sequence=[self.keyword_lookup[Colors.White.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Yellow,
                word_sequence=[self.keyword_lookup[Colors.Yellow.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Mixture,
                word_sequence=[self.keyword_lookup[Colors.Mixture.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Other,
                word_sequence=[self.keyword_lookup[Colors.Other.value],
                               self.keyword_lookup[Part.LowerBody.value]]
            ),
            # backpack
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.Accessory_Backpack,
                word_sequence=[self.keyword_lookup[Part.Backpack.value]]
            )
        ]

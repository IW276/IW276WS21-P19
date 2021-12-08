from .attribute_name import AttributeName


class SimpleAttributeExtractor:
    def __init__(self, document, attribute_name, word_sequence):
        self.document = document
        self.attribute_name = attribute_name
        self.word_sequence = word_sequence
        self.words_matched = 0

        self.document.attributes[self.attribute_name.value] = 0

    def process_word(self, word):
        if len(self.word_sequence) > 0 and word in self.word_sequence[self.words_matched]:
            self.words_matched += 1

            if self.words_matched == len(self.word_sequence):
                self.document.attributes[self.attribute_name.value] = 1
                self.words_matched = 0
        else:
            self.words_matched = 0


top_synonyms = ["shirt", "t-shirt", "top"]
pants_synonyms = ["pants", "jeans", "trousers"]


class SimpleAttributeExtractionStage:
    def process(self, document):
        text_lower = document.text.lower()
        words = text_lower.split()
        extractors = self.init_attribute_extractors(document)

        for word in words:
            for extractor in extractors:
                extractor.process_word(word)

        return [document]

    def init_attribute_extractors(self, document):
        return [
            # gender
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.Gender_Female,
                word_sequence=[["she", "her", "women", "girl"]]
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
                word_sequence=[["black", "dark"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Blue,
                word_sequence=[["blue"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Brown,
                word_sequence=[["brown"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Green,
                word_sequence=[["green"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Grey,
                word_sequence=[["grey", "gray"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Orange,
                word_sequence=[["orange"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Pink,
                word_sequence=[["pink"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Purple,
                word_sequence=[["purple"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Red,
                word_sequence=[["red"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_White,
                word_sequence=[["white", "light"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Yellow,
                word_sequence=[["yellow"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Mixture,
                word_sequence=[
                    ["colorfull", "colored", "rainbow"], top_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.UpperBody_Color_Other,
                word_sequence=[]
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
                word_sequence=[["short", pants_synonyms]]
            ),
            # pants color
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Black,
                word_sequence=[["black", "dark"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Blue,
                word_sequence=[["blue"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Brown,
                word_sequence=[["brown"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Green,
                word_sequence=[["green"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Grey,
                word_sequence=[["grey", "gray"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Orange,
                word_sequence=[["orange"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Pink,
                word_sequence=[["pink"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Purple,
                word_sequence=[["purple"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Red,
                word_sequence=[["red"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_White,
                word_sequence=[["white", "light"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Yellow,
                word_sequence=[["yellow"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Mixture,
                word_sequence=[
                    ["colorfull", "colored", "rainbow"], pants_synonyms]
            ),
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.LowerBody_Color_Other,
                word_sequence=[]
            ),
            # backpack
            SimpleAttributeExtractor(
                document=document,
                attribute_name=AttributeName.Accessory_Backpack,
                word_sequence=["backpack"]
            )
        ]

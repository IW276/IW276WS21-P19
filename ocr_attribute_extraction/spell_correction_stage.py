# import TextBlob
from textblob import TextBlob


class TextSpellCorrectionStage:  # 70% accuracy, ref.: https://textblob.readthedocs.io/en/dev/quickstart.html
    def process(self, document):
        textblob = TextBlob(document.text)
        document.text = textblob.correct().raw
        return [document]

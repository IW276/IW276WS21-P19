import re


class TextSpellCorrectionStage:
    def process(self, document):
        # Replace all newlines with spaces"
        processed = document.text.replace(
            "\r", " ").replace("\n", " ")

        # Remove abnormal characters
        processed = processed.replace("|", "I")
        processed = re.sub("[^A-Za-z0-9 .,\-%:]+", " ", processed)

        # Fix spaces around punctuation
        processed = processed.replace(',', ', ').replace(
            ' ,', ',').replace(' .', '.')

        # Remove duplicate spaces and dots
        processed = re.sub("\.(\.+)", " ", processed)
        processed = re.sub("  +", " ", processed)

        document.text = processed
        return [document]

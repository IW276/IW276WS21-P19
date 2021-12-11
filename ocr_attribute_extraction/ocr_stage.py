from tesserocr import PyTessBaseAPI

from .stage import Stage


class OCRStage(Stage):
    def __init__(self):
        Stage.__init__(self)

    def process(self, document):
        with PyTessBaseAPI() as api:
            api.SetImageFile(document.path)
            document.text = api.GetUTF8Text()
            return [document]

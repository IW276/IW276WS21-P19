from tesserocr import PyTessBaseAPI


class OCRStage:
    def process(self, document):
        with PyTessBaseAPI() as api:
            api.SetImageFile(document.path)
            document.text = api.GetUTF8Text()
            return [document]

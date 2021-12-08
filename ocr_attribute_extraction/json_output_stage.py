from ocr_attribute_extraction import document


class JsonOutputStage:
    def process(self, document):
        f = open(document.path + ".json", "w")
        f.write(document.toJson())
        f.close()
        return [document]

import json
from .stage import Stage


class JsonOutputStage(Stage):
    def __init__(self, path):
        Stage.__init__(self)
        self.path = path
        self.data = {}

    def process(self, document):
        self.data[document.path] = document.attributes
        return [document]

    def finalize(self):
        with open(self.path, "w") as f:
            f.write(json.dumps(self.data))

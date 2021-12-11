import sys
from .stage import Stage


class PrintStage(Stage):
    def __init__(self):
        Stage.__init__(self)

    def process(self, document):
        print(document, file=sys.stderr)
        return [document]

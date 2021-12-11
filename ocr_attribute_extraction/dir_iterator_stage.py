import os

from .stage import Stage
from .document import Document


class DirIteratorStage(Stage):
    def __init__(self, allowed_extensions):
        Stage.__init__(self)
        self.allowed_extensions = allowed_extensions

    def process(self, path):
        return self.scan_path(path)

    def scan_path(self, path):
        if os.path.isfile(path):
            if os.path.splitext(path)[1] in self.allowed_extensions:
                return [Document(path)]
            else:
                return []
        else:
            return [
                document
                for name in os.listdir(path)
                for document in self.scan_path(os.path.join(path, name))
            ]

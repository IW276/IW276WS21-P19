import os
from .document import Document


class DirIteratorStage:
    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions

    def process(self, dir):
        return [
            Document(os.path.join(dir, filename))
            for filename in os.listdir(dir)
            if os.path.splitext(filename)[1] in self.allowed_extensions
        ]

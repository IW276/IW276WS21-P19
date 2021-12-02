class Document:
    def __init__(self, path):
        self.path = path
        self.text = None
        self.attributes = None

    def __str__(self):
        return (
            f"# file: {self.path}\n"
            f"text: {self.text}\n"
            f"attributes: {self.attributes}"
        )

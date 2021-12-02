import textwrap


class Document:
    def __init__(self, path):
        self.path = path
        self.text = None
        self.attributes = {}

    def __str__(self):
        attributes_serialized = "\n".join([
            f"{k}: {v}"
            for k, v in self.attributes.items()
        ])

        return (
            f"# file: {self.path}\n"
            f"text:\n{textwrap.indent(self.text, '  ')}\n"
            f"attributes:\n{textwrap.indent(attributes_serialized, '  ')}"
        )

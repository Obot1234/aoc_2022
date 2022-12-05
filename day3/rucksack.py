class Rucksack:
    def __init__(self, contents: str):
        content_split = len(contents) // 2
        self.compartments = [contents[:content_split],
                             contents[content_split:]]

    def get_double_item(self) -> str:
        return set(self.compartments[0]).intersection(self.compartments[1]).pop()

    def contents(self) -> str:
        return "".join(self.compartments)

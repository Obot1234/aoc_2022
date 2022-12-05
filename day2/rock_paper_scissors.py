class RockPaperScissors:
    def __init__(self, input_line: str):
        self.first_item, self.second_item = input_line.split()

    def score(self, fun) -> int:
        return fun(self.first_item, self.second_item)

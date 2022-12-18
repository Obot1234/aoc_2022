class Monkey:
    def __init__(self, items: list[int], operation, divisible_by):
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.monkey_true = self
        self.monkey_false = self
        self.items_inspected = 0
        self.managed_worries = True

    def set_monkeys(self, monkey_true: 'Monkey', monkey_false: 'Monkey'):
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false

    def inspect(self) -> None:
        self.items_inspected += len(self.items)

        if self.managed_worries:
            new_items = [self.operation(item) // 3 for item in self.items]
        else:
            new_items = [self.operation(item) % 223092870 for item in self.items]
        self.items.clear()
        trues, falses = [], []
        for item in new_items:
            trues.append(item) if item % self.divisible_by == 0 else falses.append(item)
        self.monkey_true.extend(trues)
        self.monkey_false.extend(falses)

    def extend(self, items: list[int]):
        self.items.extend(items)

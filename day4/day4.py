from day import Day
from inputs.converter import ListConverter
from section_assignment import SectionAssignment


class Today(Day):
    def __init__(self) -> None:
        super().__init__(4)
        self.section_assignments = ListConverter(SectionAssignment).convert(self.input)

    def part1(self) -> int:
        return len([assignment for assignment in self.section_assignments if assignment.sections_overlap_fully()])

    def part2(self) -> int:
        return len([assignment for assignment in self.section_assignments if assignment.sections_overlap()])


if __name__ == '__main__':
    Today().lets_go()

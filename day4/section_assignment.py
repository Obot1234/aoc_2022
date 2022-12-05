from dataclasses import dataclass


@dataclass
class Section:
    start: int
    end: int

    def fully_contains(self, section: 'Section') -> bool:
        return self.start <= section.start and self.end >= section.end

    def contains(self, section: 'Section') -> bool:
        return self.start <= section.start <= self.end or self.start <= section.end <= self.end


class SectionAssignment:
    def __init__(self, section_assignment: str):
        sections = section_assignment.split(',')
        self.section_1 = self.parse_section(sections[0])
        self.section_2 = self.parse_section(sections[1])

    @staticmethod
    def parse_section(section: str) -> Section:
        start, end = section.split('-')
        return Section(int(start), int(end))

    def sections_overlap_fully(self) -> bool:
        return self.section_1.fully_contains(self.section_2) or self.section_2.fully_contains(self.section_1)

    def sections_overlap(self) -> bool:
        return self.section_1.contains(self.section_2) or self.section_2.contains(self.section_1)

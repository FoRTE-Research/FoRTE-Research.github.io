from dataclasses import dataclass

@dataclass
class Teaching:
    code: str
    course_name: str
    semester: str
    year: int
    link: str

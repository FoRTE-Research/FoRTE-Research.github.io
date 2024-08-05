from dataclasses import dataclass

@dataclass
class News:
    month: str
    year: int
    description: str
    link: str

from dataclasses import dataclass
from typing import Optional

@dataclass
class Publications:
    series: Optional[str]
    title: str
    author: str
    booktitle: str
    month: Optional[str]
    year: int

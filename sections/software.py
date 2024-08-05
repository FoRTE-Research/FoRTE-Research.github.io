from dataclasses import dataclass
from typing import Optional

@dataclass
class Software:
    name: str
    venue: Optional[str]
    description: str
    link: str

from dataclasses import dataclass

@dataclass
class Funding:
    title: str
    sponsor: str
    start_date: str
    end_date: str
    team: str
    total: str
    dept_share: str
    my_share: str

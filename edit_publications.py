import re
from typing import List, Tuple
from sections.publications import Publications

month_to_num = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}

# function to convert month to number for sorting
def sort_key(entry: Publications) -> Tuple:
    year = int(entry.year)
    month = month_to_num[entry.month.lower()]
    return (year, month)

def remove_braces(text: str) -> str:
    # remove braces that enclose the entire string
    text = text.strip('{} ')
    # remove remaining braces using regex
    return re.sub(r'{|}', '', text)

def clean_publication(publication_list: List) -> List:
    for field in publication_list.__dict__:
        if isinstance(getattr(publication_list, field), str):
            setattr(publication_list, field, remove_braces(getattr(publication_list, field)))
    return publication_list

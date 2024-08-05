'''
Read text files:
    News
    Software
    Teaching
    Funding
    Students

Read bibtex file:
    Publications (references.bib)
'''

from typing import List
import bibtexparser

from sections.news import News
from sections.software import Software
from sections.teaching import Teaching
from sections.funding import Funding
from sections.students import Students
from sections.publications import Publications

def read_news_file(file_path: str) -> List:
    news_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)

        for line in file:
            month, year, description, link = line.strip().split('\t')
            news_entry = News(month, year, description, link)
            news_list.append(news_entry)
    return news_list

def read_software_file(file_path: str) -> List:
    software_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)

        for line in file:
            name, venue, description, link = line.strip().split('\t')
            software_entry = Software(name, venue, description, link)
            software_list.append(software_entry)
    return software_list

def read_teaching_file(file_path: str) -> List:
    teaching_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)

        for line in file:
            code, course_name, semester, year, link = line.strip().split('\t')
            teaching_entry = Teaching(code, course_name, semester, year, link)
            teaching_list.append(teaching_entry)
    return teaching_list

def read_funding_file(file_path: str) -> List:
    funding_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)

        for line in file:
            title, sponsor, start_date, end_date, team, total, dept_share, my_share = line.strip().split('\t')
            funding_entry = Funding(title, sponsor, start_date, end_date, team, total, dept_share, my_share)
            funding_list.append(funding_entry)
    return funding_list

def read_students_file(file_path: str) -> List:
    students_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)

        for line in file:
            student_type, name, area, role, start_date, end_date, first_job, social_name, social_link, src, alt = line.strip().split('\t')
            students_entry = Students(student_type, name, area, role, start_date, end_date, first_job, social_name, social_link, src, alt)
            students_list.append(students_entry)
    return students_list

def read_publications_file(file_path: str) -> List:
    publications_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        publications_file = bibtexparser.load(file)

    for entry in publications_file.entries:
        entry_type = entry.get('ENTRYTYPE', '')
        if entry_type == 'inproceedings':
            series = entry.get('series', '')
            title = entry.get('title', '')
            author = entry.get('author', '')
            booktitle = entry.get('booktitle', '')
            month = entry.get('month', '')
            year = entry.get('year', '')
            publications_entry = Publications(series, title, author, booktitle, month, year)
            publications_list.append(publications_entry)
    return publications_list

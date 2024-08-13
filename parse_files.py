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
from openpyxl import Workbook, load_workbook
import bibtexparser

from sections.news import News
from sections.software import Software
from sections.teaching import Teaching
from sections.funding import Funding
from sections.students import Students
from sections.publications import Publications

def parse_news_sheet(sections_workbook: Workbook) -> List:
    news_sheet = sections_workbook['news']  # get specific sheet in workbook
    news_list = []

    for row in news_sheet.iter_rows(min_row=2, values_only=True):  # min_row=2 skips header line
        month, year, description, link = row
        news_entry = News(month, year, description, link)
        news_list.append(news_entry)
    return news_list

def parse_software_sheet(sections_workbook: Workbook) -> List:
    software_sheet = sections_workbook['software']
    software_list = []

    for row in software_sheet.iter_rows(min_row=2, values_only=True):
        name, venue, description, link = row
        software_entry = Software(name, venue, description, link)
        software_list.append(software_entry)
    return software_list

def parse_teaching_sheet(sections_workbook: Workbook) -> List:
    teaching_sheet = sections_workbook['teaching']
    teaching_list = []

    for row in teaching_sheet.iter_rows(min_row=2, values_only=True):
        code, course_name, semester, year, link = row
        teaching_entry = Teaching(code, course_name, semester, year, link)
        teaching_list.append(teaching_entry)
    return teaching_list

def parse_funding_sheet(sections_workbook: Workbook) -> List:
    funding_sheet = sections_workbook['funding']
    funding_list = []

    for row in funding_sheet.iter_rows(min_row=2, values_only=True):
        title, sponsor, start_date, end_date, team, total, dept_share, my_share = row
        funding_entry = Funding(title, sponsor, start_date, end_date, team, total, dept_share, my_share)
        funding_list.append(funding_entry)
    return funding_list

def parse_students_sheet(sections_workbook: Workbook) -> List:
    students_sheet = sections_workbook['students']
    students_list = []

    for row in students_sheet.iter_rows(min_row=2, values_only=True):
        student_type, name, area, role, start_date, end_date, first_job, social_name, social_link, src, alt = row
        students_entry = Students(student_type, name, area, role, start_date, end_date, first_job, social_name, social_link, src, alt)
        students_list.append(students_entry)
    return students_list

def parse_publications_bibtex(file_path: str) -> List:
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

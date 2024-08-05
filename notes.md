# A few notes on the way I've structured things

1. I created duplicate index.html and team.html files and renamed them _index.html and _team.html that are currently being referenced in freeze.py. I found that it was easier on my end for development to have the original there to reference. I can change them to index.html and team.html once everything is finalized.

2. I created an Excel spreadsheet (.xlsx file) for each of the given fields (Funding, News, Software, Students, Teaching) and saved them each as tab-delimited text files. This has been working well on my end, but if you don't want it this way I can change it. I have a folder in the project for all of the original .xlsx files and another folder for the actual tab-delimited text files. 

3. I had to change the month format for inproceedings entry "Not All Data are Created Equal..." from August to Aug to be consistent with the formatting for other entries. The bibtex parser couldn't handle it otherwise. 

4. I looked through all of the Publications entries on the current website and compared them to the contents of the references.bib file sent. All of the publications on the current site are inproceedings (except one, next point), but not all of the inproceedings were posted on the website. I wasn't sure which inproceedings you wanted posted, so currently all of the inproceedings are being posted. Please let me know if you want this adjusted.

5. On the current website there is an entry "Fall 2022 - CS 4264 - Principles of Computer Security". I couldn't find this anywhere in the references.bib file, so I left it hardcoded in the _index.html file as is. Because of this, that one date is out of order. Please let me know what you want to do with that.

6. In the Publications section, the formatting for the authors' names becomes inconsistent around year 2020 because of how it appears in the references.bib file. I'd be happy to go in and change this to be consistent with the later year entries, but did not want to make any large adjustments like this without prior approval.

7. You requested that the News & Updates section had a link for each entry but I couldn't find a link anywhere so it's currently there but empty.
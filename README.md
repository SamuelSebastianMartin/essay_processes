# essay_processes
There are two programmes used to streamline my marking workflow. Only `pdf_to_docx_essay.py` might be of any interest, but both are optimised for my university, my students and a linux system.

---

## Converting PDF files to docx: `pdf_to_docx_essay.py`
Despite my clear instructioins, students still submit PDF files. This program:

- lets you select the essy with a gui file-picker
- extracts the text from the PDF
- removes all \n line-breaks`
- does its best to put new line-breaks in the correct places

### use

`python3 pdf_to_docx_essay.py`

### issues

- the bibliography is not yet processed to remove line-breaks
- some text encodings give strange results; new correctins should be added to `finess_typography()`
- non-standard title pages are not handled

---

## Rename files to my own system: `rename_moodle_downloads.py`
Downloaded essays from Moolde have exceptionally long names. This program renames them to the conventions I use for saving work.

### use

`python3 rename_moodle_downloads.py`

### issues

seems pretty rubust, provided the start-of-year `StudWork` directory is set up.

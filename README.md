# essay_processes
There are two programmes used to streamline my marking workflow. Only `convert_pdf.py` might be of any interest, but both are optimised for my university, my students and a Linux system.

---

## Converting PDF files to docx: `convert_pdf.py`
Despite my clear instructions, students still submit PDF files. This program:

- lets you select the essay with a GUI file-picker
- extracts the text from the PDF
- removes all \n line-breaks`
- does its best to put new line-breaks in the correct places

### use

`convert_pdf.py`

### issues

- the bibliography is not yet processed to remove line-breaks
- some text encodings give strange results; new corrections should be added to `finesse_typography()`
- non-standard title pages are not handled

---

## Rename files to my own system: `rename_moodle_downloads.py`
Downloaded essays from Moolde have exceptionally long names. This program renames them to the conventions I use for saving work.

### use

`python3 rename_moodle_downloads.py`

### issues

Seems pretty robust, provided the start-of-year `StudWork` directory is set up.

---

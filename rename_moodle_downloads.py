#! /usr/bin/env python3

'''This renames files which have been downloaded from a Moodle course
according to my personal naming convention.

It works from the list of students in the StudWork/ directory, based on their
first entry (eg 'aa00 FirstName MidNames LastName'), and will not alter any
filenames unless both the students FirstName and LastName are in present.
Therefore there is almost no chance of renaming the wrong file.

File extensions are preserved, so files with identical names are handled well.
eg 'FILE NAME.odt' and 'FILE NAME.pdf' are processed accurately.

It assumes that Moodle will give both first and second names in their filename
It requires user input to provide the week_number and work_description
which will appear in the new_filename after the student identifier code;
eg '05tw' -> 'aa05tw.pdf' or similar.
'''

import os
import re


def main():
    name00 = re.compile(r'[a-z]{2}00.+')
    extension = re.compile(r'\.[a-z]{3}.?$')  # Finds 2-3 digit file extension

    work_piece = get_work_name()
    codes = get_student_codes(name00)
    files = get_current_essay_names(extension)
    pairs = pair_names(codes, files, work_piece, extension)
    rename(pairs)


def get_work_name():
    work_piece = input('''
    This program will rename files downloaded from Moodle.
    It assumes:
        1. That Moodle saves with both first and second name in the filename.
        2. That the StudWork file is set up with student names and id's.


    What is the number and title of the work. 
    eg for 'aa05tw.pdf' you should enter '05tw'
    ''')
    return work_piece


def get_student_codes(name00):
    '''Reads StudWork dir, and returns dictionary of {id: name}'''
    codes = {}
    listdir = os.listdir('/home/sam/SOAS/AcEng/StudWork/')
    for stud in listdir:
        if name00.search(stud):
            codes.update({stud[:2]: stud[5:]})
    return codes


def get_current_essay_names(extension):
    '''Returns list of files in CWD which could be essays. (not .py, .sh)'''
    files = []
    listdir = os.listdir()
    for item in listdir:
        if extension.search(item):
            files.append(item)
    return(files)


def pair_names(codes, files, work_piece, extension):
    '''returns tuple ready for naming: (id, workname, .ext, filename)'''
    pairs = []
    for code, name in codes.items():
        first_name = name.split()[0].lower()
        last_name = name.split()[-1].lower()
        for filename in files:

            dot_ext_srch = extension.search(filename)
            dot_ext = dot_ext_srch.group()

            lowname =  filename.lower()
            if first_name in lowname and last_name in lowname:
                pairs.append((code, work_piece, dot_ext, filename))
    return pairs


def rename(pairs):
    for pair in pairs:
        new_filename = pair[0] + pair[1] + pair[2]
        old_filename = pair[-1]
        os.rename(old_filename, new_filename)
        print(old_filename, 'has been renamed ', new_filename)



if __name__ == '__main__':
    main()

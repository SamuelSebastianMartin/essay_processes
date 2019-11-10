#! /usr/bin/env python3

from textblob import TextBlob

#  Open the Complete Essay
with open('essay_complete.txt', 'r') as fcomp:
    essay_complete = fcomp.read()
#  Open the Essay Parts
with open('essay_parts/bibliog.txt', 'r') as f:
    bibliog = f.read()
with open('essay_parts/body_paras.txt', 'r') as f:
    body_paras = f.read()
with open('essay_parts/conc.txt', 'r') as f:
    conc = f.read()
with open('essay_parts/essay_core.txt', 'r') as f:
    essay_core = f.read()
with open('essay_parts/intro.txt', 'r') as f:
    intro = f.read()
with open('essay_parts/question.txt', 'r') as f:
    question = f.read()
with open('essay_parts/thesis.txt', 'r') as f:
    thesis = f.read()
with open('essay_parts/titlepage.txt', 'r') as f:
    titlepage = f.read()


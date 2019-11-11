#! /usr/bin/env python3

from textblob import TextBlob
import nltk
import Essay


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

fine_paras = essay_complete.splitlines()
print(len(fine_paras))
paras = []
for para in fine_paras:
    if len(para) != 0:
        paras.append(para)


#blob = TextBlob(essay_complete)
#sentences = blob.sentences
#paras = blob.split('.\n')
print('Number of Paras = ', len(paras))
for para in paras:
    print()
    print(len(para), para[:50])

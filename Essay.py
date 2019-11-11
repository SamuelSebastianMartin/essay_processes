#! /usr/bin/env python3

class Essay:
    """
    This class takes a plain text essay, and
    It aims to break it into logical sections,
    each returned in plain text:

        *  Title Page
           - Question
        *  Essay
           -  Introduction
           -  Thesis Statement
           -  Body paragraphs
           -  conclusion
        *  Bibliography
           -  Individual References

    As this is not a definitive task, probability
    is used: for each section, a series of likely
    identifiers is tested for, and each of these
    identifying parameters lends support to the
    hypothesis that the section is or is not the
    section being tested for.
    """

    def locate_biblio(self):
        """
        Searched for first, because easiest to find.
        Parameters:
        *  Consists of several short lines.
        *  Contains date on each line.
        *  Lines begin with capitalised surname.
        *  Contains capitalised initials plus full stop.
        *  Contains high percentage of punctuation.
        *  Contains proper nouns (or spell-errors).
        """
        pass

    def locate_titlepage(self):
        """
        Parameters:
        *  Has many short paragraphs.
        *  Most sentences are short.
        *  Has keywords ['title', 'name', etc]
        *  Has at least 2 of 'word', 'count', <number>.
        """
        pass

    def locate_question(self):
        """
        Parameters:
        *  One or two sentences
        *  Ends in a question mark
        *  Includes words like ['discuss', 'extent', etc]
        *  Longest sentence, if title page is 3-4 lines.
        *  Shares words with the thesis.
        *  Includes labeling words like ['title' etc]
        """
        pass

    def locate_intro(self):
        """
        Parameters:
        *  Is more than 30 words long.
        *  Contains thesis words ['this', 'essay', etc].
        *  Contains words from question near end of paragraph.
        *  Comes before all body paras, conc and bibliography
           - could be 2 paras, if there are many body paras.
        *  Comes after title page
        """
        pass

    def locate_thesis(self):
        """
        Parameters:
        *  One or two sentences
        *  Shares words with the question.
        *  Contains thesis words ['this', 'essay', etc].
        *  Situated near the end of the introduction.
        """
        pass

    def locate_conc(self):
        """
        Parameters:
        *  Is more than 30 words long.
        *  Contains thesis words ['has', 'essay', etc].
        *  Contains words from question words near start.
        *  Comes after title page, intro & all body paras.
           - could be 2 paras, if many body paras.
        *  Comes before the bibliography.
        """
        pass

#!/usr/bin/env python3
import re
def contains_acronym(text):
    pattern = r"\([A-Z0-9][a-zA-Z0-9]+\)"
    result = re.search(pattern, text)
    return result != None
print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))
print(contains_acronym("Please do NOT enter without permission!"))
print(contains_acronym(
    "PostScript is a fourth-generation programming language (4GL)"))
print(contains_acronym(
    "Have fun using a self-contained underwater breathing apparatus (Scuba)!"))

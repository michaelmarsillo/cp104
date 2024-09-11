"""
-------------------------------------------------------
[Lab 10, Task 11]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

fh = open("words.txt", "r", encoding="utf-8")

print(
    f"file 'words.txt' open for reading\n'{find_longest(fh)}' is the last longest word")
fh.close()

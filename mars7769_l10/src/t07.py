"""
-------------------------------------------------------
[Lab 10, Task 7]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num

fh = open("numbers.txt", "r+", encoding="utf-8")

print(f"file 'numbers.txt' open for reading and writing \n{append_max_num(fh)} is appended")
fh.close()

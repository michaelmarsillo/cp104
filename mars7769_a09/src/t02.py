"""
-------------------------------------------------------
[Assignment 9, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-28"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

file_handle = open("numbers.txt", "r", encoding="utf-8")

result = read_integers(file_handle)
print(result)

file_handle.close()

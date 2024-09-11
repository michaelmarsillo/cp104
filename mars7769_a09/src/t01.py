"""
-------------------------------------------------------
[Assignment 9, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-28"
-------------------------------------------------------
"""
# Imports
from functions import file_top

file_handle = open("students.txt", "r", encoding="utf-8")
file_top(file_handle, 5)
file_handle.close()

"""
-------------------------------------------------------
[Assignment 9, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-28"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")


result = file_statistics(file_handle)
print(result)

file_handle.close()

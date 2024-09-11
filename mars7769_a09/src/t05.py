"""
-------------------------------------------------------
[Assignment 9, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-29"
-------------------------------------------------------
"""
# Imports
from functions import student_stats

with open("students.txt", "r") as file_handle:
    l_id, h_id, avg = student_stats(file_handle)
    print(f"{l_id}, {h_id}, {avg}")

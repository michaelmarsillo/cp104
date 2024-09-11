"""
-------------------------------------------------------
[Lab 11, Task 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

matrix = [[2, 0, -1, 1], [10, 4, -5, 9], [-6, 3, 6, 0]]
result = matrix_stats(matrix)
print(f"Smallest: {result[0]}")
print(f"Largest: {result[1]}")
print(f"Total: {result[2]}")
print(f"Average: {result[3]}")

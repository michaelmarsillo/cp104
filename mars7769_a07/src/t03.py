"""
-------------------------------------------------------
[Assignment 7, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports
from functions import get_indexes

# inputs
target_number = int(input("Target number: "))
numbers = [5, 1, 8, 9, 5, 2, 5, 3]
index_list = get_indexes(numbers, target_number)
print(index_list)

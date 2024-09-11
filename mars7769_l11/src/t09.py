"""
-------------------------------------------------------
[Lab 11, Task 9]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency

matrix = [['g', 'h', 'a', 'd'], ['o', 't', 'n', 'd'], ['w', 'j', 't', 'c']]
char = 'd'
result = count_frequency(matrix, char)
print(f"The character '{char}' appeared {result} times.")

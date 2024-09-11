"""
-------------------------------------------------------
[Lab 11, Task 14]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
from functions import matrix_transpose


matrix = [[6, 4, 24], [1, -9, 8]]
transposed_matrix = matrix_transpose(matrix)
print("Original Matrix:")
for row in matrix:
    print('\t'.join(map(str, row)))

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print('\t'.join(map(str, row)))

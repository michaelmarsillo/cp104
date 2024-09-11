"""
-------------------------------------------------------
[Lab 6, Task 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports
from functions import draw_triangle

# inputs
height = int(input("Enter the number of rows:"))
char = str(input("Enter the character you want the triangle drawn: "))

result = draw_triangle(height, char)
print(result)

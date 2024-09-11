"""
-------------------------------------------------------
[Lab 4, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports

from functions import square_pyramid

b = float(input(f"Enter Base: "))
h = float(input(f"Enter Height: "))

result = square_pyramid(b, h)
print(result)

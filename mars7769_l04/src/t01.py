"""
-------------------------------------------------------
[Lab 4, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-03"
-------------------------------------------------------
"""
# Imports
from functions import diameter


# Constants

rad = float(input("Enter radius: "))
print()
dia = diameter(rad)
print(f"Diameter of circle: {dia:.1f}")

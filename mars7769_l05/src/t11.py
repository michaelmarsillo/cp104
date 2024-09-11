"""
-------------------------------------------------------
[Lab 5, Task 11]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports
from functions import quadrant


# Input
x = float(input("'X' coordinate on a Cartesian plane: "))
y = float(input("'Y' coordinate on a Cartesian plane: "))

# Output
location = quadrant(x, y)
print(f"Location: {location}")

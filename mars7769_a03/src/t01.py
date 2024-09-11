"""
-------------------------------------------------------
[Assignment 3, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres

sqaure_feet = float(input("Enter the area in square feet: "))

result = footage_to_acres(sqaure_feet)
print(
    f"The conversion of {sqaure_feet} square feet to acres is equal to {result} acres. ")

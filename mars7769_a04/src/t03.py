"""
-------------------------------------------------------
[Assignment 4, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports
from functions import largest_average

# inputs
val1 = float(input("Enter a number: "))
val2 = float(input("Enter a number: "))
val3 = float(input("Enter a number: "))

# outputs
result = largest_average(val1, val2, val3)
print(f"The largest average of the three numbers is {result}")

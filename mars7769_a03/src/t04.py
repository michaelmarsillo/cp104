"""
-------------------------------------------------------
[Assignment 3, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions

# inputs
num1 = int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction: "))
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction: "))

# outputs
answer = multiply_fractions(num1, den1, num2, den2)
print(answer)

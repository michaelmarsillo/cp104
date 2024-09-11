"""
-------------------------------------------------------
[Lab 6, Task 15]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports
from functions import statistics

# inputs
n = int(input("Enter the number of values to process: "))

# outputs
minimum, maximum, total, average = statistics(n)
print(f"Minimum: {minimum:.2f}")
print(f"Maximum: {maximum:.2f}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")

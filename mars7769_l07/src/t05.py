"""
-------------------------------------------------------
[Lab 7, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports
from functions import positive_statistics

minimum, maximum, total, average = positive_statistics()

print(
    f"Minimum: {minimum:.2f}, Maximum: {maximum:.2f}, Total: {total:.2f}, Average: {average:.2f}")

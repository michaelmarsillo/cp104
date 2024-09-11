"""
-------------------------------------------------------
[Lab 5, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports
from functions import is_leap

# Constants

year = int(input("Enter a year: "))

result = is_leap(year)
print(f"Is {year} a leap year? {result}.")

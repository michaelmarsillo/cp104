"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import extract_date

# inputs
date_number = int(input(f"Enter a date in the format YYYYMMDD: "))

# outputs
result = extract_date(date_number)
print(result)

"""
-------------------------------------------------------
[Assignment 2, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports

# Constants

date = int(input(f"Enter a date in the format YYYYMMDD: "))
year = date // 10000
month = (date // 100) % 100
day = date % 100


print()
print(f"The reformatted date: {year}/{month}/{day}")

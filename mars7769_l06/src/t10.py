"""
-------------------------------------------------------
[Lab 6, Task 10]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports
from functions import treadmill

# inputs
burnt_per_minute = float(input("Enter the calories burnt per minute: "))
start = int(input("Enter the start time in minutes: "))
end = int(input("Enter the end time in minutes: "))
inc = int(input("Enter the increments time in minutes: "))

# outputs
result = treadmill(burnt_per_minute, start, end, inc)
print(result)

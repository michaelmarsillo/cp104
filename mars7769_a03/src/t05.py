"""
-------------------------------------------------------
[Assignment 3, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import falling_distance

# inputs
falling_time = int(
    input("Enter the time the object has fallen in seconds: "))

distance = falling_distance(falling_time)
print(f"The distance the object has fallen in metres is {distance}")

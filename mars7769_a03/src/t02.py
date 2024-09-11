"""
-------------------------------------------------------
[Assignment 3, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mow_time

# inputs
width = float(input("Enter the width of the lawn in metres: "))
length = float(input("Enter the length of the lawn in metres: "))
speed = float(input("Enter the speed of the lawn in minutes: "))

# outputs
time = lawn_mow_time(width, length, speed)
print(f"The time required to mow the lawn is {time} minutes")

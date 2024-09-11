"""
-------------------------------------------------------
[Assignment 2, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-03"
-------------------------------------------------------
"""
# Imports

# Constants


number = int(input(f"Enter a positive two-deigit integer: "))

# seperate the 2 numbers
left_digit = number // 10
right_digit = number % 10

# find difference
difference = (left_digit) - (right_digit)

print()
print(f"The difference of the digits of 25 is {difference}")

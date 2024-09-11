"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports

# Constants

flyers = int(input(f"Enter the number of flyers: "))
delivery_people = int(input(f"Enter the number of delivery people: "))

flyers_per_person = (flyers) // (delivery_people)
flyers_left_over = (flyers) % (delivery_people)

print()
print()
print(f"Flyers per delivery person: {flyers_per_person}")
print(f"Flyers left over: {flyers_left_over}")

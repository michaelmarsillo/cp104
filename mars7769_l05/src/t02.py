"""
-------------------------------------------------------
[Lab 5, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports
from functions import get_weight

# Constants

mass = float(input("Enter the mass of the object: "))

weight, message = get_weight(mass)
print(
    f"The weight of your objects mass is {weight:.2f} Newtons, which is considered {message}.")

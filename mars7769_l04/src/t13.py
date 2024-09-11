"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports

from functions import f_to_c


# Constants

fahrenheit = int(input(f"Enter the temperature in Fahrenheit: "))
celsius = f_to_c(fahrenheit)
print(celsius)

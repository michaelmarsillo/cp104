"""
-------------------------------------------------------
[Lab 2, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """

    # Constants
WATER_FREEZE_FAHRENHEIT = 32


fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

celcius = (fahrenheit - 32) * 5/9
print(celcius)

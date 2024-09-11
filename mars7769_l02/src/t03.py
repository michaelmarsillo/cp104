"""
-------------------------------------------------------
[Lab 2, Task 3]
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
LARGE_DOG = 75  # Dollars
SMALL_DOG = 50


num_of_large = int(input("Enter number of Large dogs groomed today: "))

num_of_small = int(input("Enter number of Small dogs groomed today: "))


total = (num_of_large * LARGE_DOG) + (num_of_small * SMALL_DOG)
print(f"Total money earned for the day: {total}$")

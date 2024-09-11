"""
-------------------------------------------------------
[Assignment 8, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-22"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn

# inputs
isbn = str(input("Enter an isbn: "))

# outputs
result = valid_isbn(isbn)
print(result)

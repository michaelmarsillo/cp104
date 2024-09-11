"""
-------------------------------------------------------
[Lab 9, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-15"
-------------------------------------------------------
"""
# Imports
from functions import validate_code

# Constants

product_code = str(input("Enter product code: "))

result = validate_code(product_code)

print(result)

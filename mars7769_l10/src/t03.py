"""
-------------------------------------------------------
[Lab 10, Task 3]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_best

# open file
fh = open("customers.txt", "r", encoding="utf-8")

result = customer_best(fh)
print("Find customer with largest balance: ")
print(result)

"""
-------------------------------------------------------
[Lab 10, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_record

# open the file
fh = open("customers.txt", "r", encoding="utf-8")

# input
n = int(input("The number of the record to return: "))

# output
result = customer_record(fh, n)
print(result)
fh.close()

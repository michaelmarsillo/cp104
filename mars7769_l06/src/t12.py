"""
-------------------------------------------------------
[Lab 6, Task 12]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports
from functions import gic

# inputs
value = int(input("Enter the GIC's initial value: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the percent increase value per year: "))

# outputs
result = gic(value, years, rate)
print(result)

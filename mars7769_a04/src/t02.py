"""
-------------------------------------------------------
[Assignment 4, Task 2]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports
from functions import pollution_ranking

# inputs
air_quality_index = int(input("Enter the Air Quality Index: "))

# outputs
result = pollution_ranking(air_quality_index)
print(f"The pollution level is {result}")

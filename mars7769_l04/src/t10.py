"""
-------------------------------------------------------
[Lab 4, Task 10]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports
from functions import population

# Constants


pop_size = int(input(f"Enter current population: "))
average_births_second = int(input(f"Enter average births between seconds: "))
average_deaths_second = int(input(f"Enter average deaths between seconds: "))
average_immigrant_second = int(
    input(f"Enter average seconds between immigrants: "))
years_to_calculate = int(
    input(f"Enter average years to calculate new population: "))

new_population = population(pop_size, average_births_second,
                            average_deaths_second, average_immigrant_second, years_to_calculate)
print(new_population)

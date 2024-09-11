"""
-------------------------------------------------------
[Lab 8, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""
# Imports
from functions import get_weekday_name

for i in range(1, 8):
    day_number = int(input("Enter the day of the week in a number: "))
    day_name = get_weekday_name(day_number)
    print(f"{day_number} = {day_name}")

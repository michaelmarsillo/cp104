"""
-------------------------------------------------------
[Lab 7, Task 10]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# Imports
from functions import employee_payroll

total, average = employee_payroll()

print(f"Total net wages: ${total:.2f}")
print(f"Average net wages: ${average:.2f}")

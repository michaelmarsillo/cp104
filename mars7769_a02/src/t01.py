"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports

# Constants
ANNUAL_TAX = 18.5

projected_total = float(input(f"Enter the total projected sales: "))
total_tax = (projected_total) * (ANNUAL_TAX/100)

print()
print(f"Projected Tax Report")
print(f"--------------------------")
print(f"Total sales:   $ {projected_total:,.2f}")
print(f"Annual tax:    % {ANNUAL_TAX:.2f}")
print(f"--------------------------")
print(f"Tax:           $ {total_tax:,.2f}")

"""
-------------------------------------------------------
[Assignment 1, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports

# Constants


principal_amount = float(input("Principal: "))
interest_rate_annual = float(input("Interest (%) "))
number_of_years = int(input("Number of years: "))
number_of_compounds = int(
    input("Number of times interest compounded per year: "))

interest_rate_annual = (interest_rate_annual) / 100

amount_accumulated = (1 + (interest_rate_annual) / (number_of_compounds)
                      ) ** (number_of_compounds * number_of_years) * (principal_amount)


print(f"Balance: {amount_accumulated} ")

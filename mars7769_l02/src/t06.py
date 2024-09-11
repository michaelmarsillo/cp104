"""
-------------------------------------------------------
[Lab 2, Task 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


principal_amount = float(
    input("Enter the mortgage principal amount: "))  # Dollars
number_of_years = int(
    input("Enter the number of years the mortgage will run: "))  # Years
yearly_interest = int(input("Enter the yearly interest rate: "))  # Percent

monthly_interest = (yearly_interest / 100) / 12
number_of_months = number_of_years * 12


numerator = monthly_interest * (1 + monthly_interest) ** number_of_months
denominator = (1 + monthly_interest) ** number_of_months - 1

monthly_payment = (numerator / denominator) * principal_amount
print(f"The monthly payments are: {monthly_payment}$")

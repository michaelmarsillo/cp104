"""
-------------------------------------------------------
[Lab 5, Task 14]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports
from functions import ticket

ticket_price = ticket()
if ticket_price is not None:
    print(f"The ticket price is ${ticket_price:.2f}")

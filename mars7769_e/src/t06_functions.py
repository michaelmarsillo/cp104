"""
-------------------------------------------------------
Exam Task 6 Function Definitions
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def multiply_list(values):
    """
    -------------------------------------------------------
    Multiplies the value of each element of values by its index.
    Use: multiply_list(values)
    -------------------------------------------------------
    Parameters:
        values - list of elements to multiply (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌‌​‌‌‌‌​‌​​‌:
        None
    -------------------------------------------------------
    """

    # Your code here
    index = values

    for i in range(len(values)):
        values[i] *= i

    return index

"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌‌​‌‌‌‌​‌​​‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """

    # your code here
    even_numbers = [num for num in values if num % 2 == 0]

    sum_even = sum(even_numbers)

    count_even = len(even_numbers)

    if count_even > 0:
        average_even = sum_even // count_even
    else:
        average_even = 0

    return average_even

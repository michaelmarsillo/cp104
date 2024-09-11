"""
-------------------------------------------------------
[Lab 8]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-06"
-------------------------------------------------------
"""
# Imports
from random import randint


# Constants
DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    return DAYS_OF_WEEK[d - 1]


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    numbers = []

    while len(numbers) < n:
        rand_num = randint(low, high)

        if rand_num not in numbers:
            numbers.append(rand_num)

    numbers.sort()
    return numbers


def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """
    index = 0
    length = len(values)
    result = -1

    while index < length:

        if values[index] == value:
            result = index
            break
        index += 1

    return result


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    for i in range(len(source1)):
        target.append(source1[i] + source2[i])

    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    source1_set = set(source1)
    source2_set = set(source2)

    common_elements = source1_set.intersection(source2_set)
    target = list(common_elements)
    return target

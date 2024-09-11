"""
-------------------------------------------------------
[Lab 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0

    for i in range(1, num + 1, 2):
        total += i

    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, height + 1):
        print(" " * (height - i) + char * (2 * i - 1))
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for time in range(start, end + 1, inc):
        calories_burned = burnt_per_minute * time
        print(f"Calories burned after {time} minutes: {calories_burned:.1f}")
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print("Year       Value $")
    print("------------------")
    for year in range(years + 1):
        value_with_comma = f"{value:,.2f}"
        print(f"{year:<10}{value_with_comma:>10}")
        final_value = value
        value *= (1 + rate / 100)
        final_value = float(f"{final_value:.2f}")
    return final_value


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    total = 0
    minimum = None
    maximum = None

    for i in range(n):
        value = float(input("Next value: "))  # Prompt the user for input
        total += value  # Add the value to the total

        # Update the minimum and maximum
        if minimum is None or value < minimum:
            minimum = value
        if maximum is None or value > maximum:
            maximum = value

    # Calculate the average
    average = total / n

    return minimum, maximum, total, average

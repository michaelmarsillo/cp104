"""
-------------------------------------------------------
[Assignment 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints the number of calories burned every five minutes 
    given the number of calories burned per minute.
    Use: calories_burned = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number of calories burned per min (int > 0)
        minutes - total number of minutes (int > 0)
    Returns:
        calories_burned - number of colories burned over the time
    ------------------------------------------------------
    """
    for time in range(5, minutes + 1, 5):
        calories_burned = per_min * time
        print(f"{time}  {calories_burned:.1f}")
    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Print an arrow poniting up with '#' characters.
    Use: result = arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the height of the arrow (int)
    Returns:
        None: prints the arrow
    ------------------------------------------------------
    """
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            print(f"{spaces}#")
        else:
            inner_spaces = " " * (2 * i - 3)
            print(f"{spaces}#{inner_spaces}#")
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start_num, stop_num + 1):
        if i == start_num:
            # Print the header row with the column numbers
            print(" " * 7, end="")
            for j in range(start_num, stop_num + 1):
                print(f"{j:5}", end="")
            print("\n" + " " * 7 + "-" * 21)

        for j in range(start_num, stop_num + 1):
            if j == start_num:
                # Print the row label
                print(f"{i:2} |", end="")

            # Print the multiplication result
            print(f"{i * j:5}", end="")
        print()
    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total += start
        start += increment
    return total

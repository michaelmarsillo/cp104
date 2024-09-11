"""
-------------------------------------------------------
[Lab 11]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-26"
-------------------------------------------------------
"""
# Imports
import random


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    if value_type == 'float':
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(random.uniform(low, high))
            matrix.append(row)
    elif value_type == 'int':
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(random.randint(low, high))
            matrix.append(row)
    else:
        raise ValueError("Invalid value_type. Use 'float' or 'int'.")

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    if value_type not in ('float', 'int'):
        raise ValueError("Invalid value_type. Use 'float' or 'int'.")

    if not matrix:
        print("Empty matrix")
        return

    max_lengths = [max(len(f"{elem:.2f}" if value_type == 'float' else str(
        elem)) for elem in col) for col in zip(*matrix)]

    print("      ", end="")
    for i in range(len(matrix[0])):
        print(f"{i:6}", end="")
    print()

    for i, row in enumerate(matrix):
        print(f"{i:2}  ", end="")
        for j, elem in enumerate(row):
            if value_type == 'float':
                print(f"{elem:6.2f}", end="")
            else:
                print(f"{elem:6}", end="")
        print()


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = float('inf')
    largest = float('-inf')
    total = 0
    count = 0

    for row in matrix:
        for num in row:
            if isinstance(num, (int, float)):
                smallest = min(smallest, num)
                largest = max(largest, num)
                total += num
                count += 1

    average = total / count if count > 0 else 0

    return smallest, largest, total, average


def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    count = 0
    for row in matrix:
        if isinstance(row, list):
            for element in row:
                if isinstance(element, str) and len(element) == 1:
                    if element == char:
                        count += 1

    return count


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

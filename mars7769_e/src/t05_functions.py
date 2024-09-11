"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌‌​‌‌‌‌​‌​​‌:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # Your code here

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    with open("numbers.txt", 'r') as file:
        values = [int(val) for val in file.read().split()]

    for i in range(rows):
        for j in range(cols):
            if values:
                matrix[i][j] = values.pop(0)

    return matrix

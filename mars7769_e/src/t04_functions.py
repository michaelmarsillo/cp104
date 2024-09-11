"""
-------------------------------------------------------
Exam Task 4 Function Definitions
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def draw_x(height):
    """
    -------------------------------------------------------
    Prints a X shape height characters high.
    Use: draw_x(height)
    -------------------------------------------------------
    Parameters:
        height - maximum height in characters of X shape (int >= 3)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌‌​‌‌‌‌​‌​​‌:
        None
    -------------------------------------------------------
    """

    # Your code here
    for i in range(height):
        for j in range(height):
            if i == j or i + j == height - 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()

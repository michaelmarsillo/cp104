"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌‌​‌‌‌‌​‌​​‌:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    # Your code here
    vowels = "aeiou"
    altered = ""

    for char in string:
        if char.lower() in vowels:
            altered += char.upper()
        elif char.isalpha():
            altered += char.lower()
        else:
            altered += char

    return altered

"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# your imports here
from t07_functions import line_lengths


# Your code here
with open('source.txt', 'r') as f_in, \
        open('output_file_1.txt', 'w') as f_short, \
        open('output_file_2.txt', 'w') as f_long:

    n = 16

    lines_file1, lines_file2 = line_lengths(
        f_in, f_short, f_long, n)

    print(f"Number of lines in output file 1: {lines_file1}")
    print(f"Number of lines in output file 2: {lines_file2}")

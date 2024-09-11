"""
-------------------------------------------------------
[Assignment 9, Task 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-29"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering

input_filename = "wilde.txt"
output_filename = "wilde_numbered.txt"

# Open files and use the function to add line numbering
with open(input_filename, "r") as read_file, open(output_filename, "w") as write_file:
    line_numbering(read_file, write_file)

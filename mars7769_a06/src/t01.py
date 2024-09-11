"""
-------------------------------------------------------
[Assignment 6, Task 1]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports
from functions import total_wins

if __name__ == "__main__":
    purple_count, gold_count = total_wins()
    print(f"({purple_count}, {gold_count})")

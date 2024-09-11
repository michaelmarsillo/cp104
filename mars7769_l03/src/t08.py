"""
-------------------------------------------------------
[Lab 3, Task 8]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

# Constants
dirt = float(input("Enter the amount of dirt (m^3):"))
gravel = float(input("Enter the amount of gravel (m^3):"))
sand = float(input("Enter the amount of sand (m^3):"))

# total is the sum of the 3
total = dirt + gravel + sand

print(f"Material   Cubic Metres")
print(f"Dirt   {dirt:9.1f}")
print(f"Gravel {gravel:9.1f}")
print(f"Sand   {sand:9.1f}")
print(f"Total  {total:9.1f}")

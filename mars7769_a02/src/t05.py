"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports

# Constants

# foundation
length = float(input(f"Enter foundation length: "))
width = float(input(f"Enter foundation width: "))
foundation_height = float(input(f"Enter foundation height: "))

# wall
wall_height = float(input(f"Enter wall height: "))

# costs
concrete_cost = float(input(f"Enter cost of concrete ($/m^3): "))
bricks_cost = float(input(f"Enter cost of concrete ($/m^2): "))

# foundation calculations
foundation_vol = (length) * (width) * (foundation_height)
foundation_cost = ((length) * (width) * (foundation_height)) * (concrete_cost)

# bricks calculations
bricks_needed = (2 * (length) * (wall_height)) + (2 * (width) * (wall_height))
cost_of_bricks = ((2 * (length) * (wall_height)) +
                  (2 * (width) * (wall_height))) * (bricks_cost)

# total
total_cost = (foundation_cost) + (cost_of_bricks)

print()
print(f"Concrete needed for foundation (m^3): {foundation_vol:.2f}")
print(f"Cost of concrete: ${foundation_cost:.2f}")
print(f"Bricks needed for walls (m^2): {bricks_needed:.2f}")
print(f"Cost of bricks: ${cost_of_bricks:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")

"""
-------------------------------------------------------
[Lab 2, Task 12]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports

# Constants
MINUTE = 60  # seconds
HOUR = 60  # minutes
DAY = 24  # hours


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


total_seconds = int(input("Enter the total amount of seconds: "))

# calculations
days = total_seconds // 86400  # seconds in a day
remaining_seconds = total_seconds % 86400

hours = remaining_seconds // 3600  # seconds in an hour
remaining_seconds %= 3600

minutes = remaining_seconds // 60  # 60 seconds in a minute
seconds = remaining_seconds % 60

# print result
print(f"Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {seconds}")

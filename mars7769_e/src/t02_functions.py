"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Michael Marsillo
ID:     169057769
Email:  mars7769@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Constants

# Your constants here
DRY_THRESHOLD = 4
DAMP_THRESHOLD = 8


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: DRY_DAYS, DAMP_DAYS, WET_DAYS, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​​‌‌‌​‌‌‌‌​‌​​‌:
        DRY_DAYS - number of dry days (int)
        DAMP_DAYS - number of damp days (int)
        WET_DAYS - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    # your code here
    total_rainfall = 0
    dry_days = 0
    damp_days = 0
    wet_days = 0
    count = 0

    while True:
        rainfall = int(
            input("Enter daily rainfall in mm (enter -1 to stop): "))

        if rainfall == -1:
            break

        total_rainfall += rainfall
        count += 1

        if rainfall < DRY_THRESHOLD:
            dry_days += 1
        elif DRY_THRESHOLD <= rainfall <= DAMP_THRESHOLD:
            damp_days += 1
        else:
            wet_days += 1

    if count == 0:
        avg = 0
    else:
        avg = total_rainfall // count

    return dry_days, damp_days, wet_days, avg

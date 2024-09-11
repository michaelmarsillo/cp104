"""
-------------------------------------------------------
[Lab 5]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports

# Constants
GRAVITY = 9.8


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight = mass * (GRAVITY)

    if weight > 1000:
        message = "heavy"
    elif weight < 10:
        message = "light"
    else:
        message = "average"

    return weight, message


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    return is_leap_year


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """

    if n == 1:
        numeral = 'I'
    elif n == 2:
        numeral = 'II'
    elif n == 3:
        numeral = 'III'
    elif n == 4:
        numeral = 'IV'
    elif n == 5:
        numeral = 'V'
    elif n == 6:
        numeral = 'VI'
    elif n == 7:
        numeral = 'VII'
    elif n == 8:
        numeral = 'VIII'
    elif n == 9:
        numeral = 'IX'
    elif n == 10:
        numeral = 'X'
    else:
        numeral = None

    return numeral


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    if x == 0 and y == 0:
        location = 'Origin'
    elif x == 0:
        location = 'Y-Axis'
    elif y == 0:
        location = 'X-Axis'
    elif x > 0:
        if y > 0:
            location = 'Quadrant 1'
        else:
            location = 'Quadrant 4'
    else:
        if y > 0:
            location = 'Quadrant 2'
        else:
            location = 'Quadrant 3'
    return location


# Constants
INFANT = 2
SENIOR = 65
STUDENT_MIN_AGE = 10
STUDENT_MAX_AGE = 18
ADULT_MIN_AGE = 18
ADULT_MAX_AGE = 65
KID_MIN_AGE = 3


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = int(input("How old are you? "))

    if age < INFANT:
        price = 0.00
    elif age >= SENIOR:
        price = 4.00
    elif STUDENT_MIN_AGE <= age < STUDENT_MAX_AGE:
        student_response = input("Are you a student at the school (Y/N)? ")
        if student_response == "Y":
            price = 1.00
        elif student_response == "N":
            price = 3.00
        else:
            print("Invalid student response (Y/N)")
    elif ADULT_MIN_AGE <= age < ADULT_MAX_AGE:
        price = 5.00
    elif KID_MIN_AGE <= age:
        price = 2.00
    else:
        print("Invalid age")

    return price

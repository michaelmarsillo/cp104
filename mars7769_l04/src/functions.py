"""
-------------------------------------------------------
[Lab 4]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports
import math


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    diam = radius * 2
    return diam


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sh = math.sqrt((base/2)**2 + (height)**2)
    area = (base**2) + 2 * (base) * math.sqrt(((base)**2/4) + (height) ** 2)
    vol = ((base)**2) * ((height)/3)

    return sh, area, vol


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    # calculate hypotenuse
    hypotenuse = math.sqrt((s1)**2 + (s2)**2)

    radius = hypotenuse

    diam = (radius) * 2
    circ = 2 * (math.pi) * (radius)
    area = (math.pi) * ((radius)**2)

    return radius, diam, circ, area


# Constants
TOTAL_SECONDS_PER_YEAR = 31536000


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """

    # total seconds
    total_birth_seconds = (TOTAL_SECONDS_PER_YEAR / births)
    total_death_seconds = (TOTAL_SECONDS_PER_YEAR / deaths)
    immigrants_per_year = (TOTAL_SECONDS_PER_YEAR / immigrants)

    # calculate the change in population
    pop_change = total_birth_seconds - total_death_seconds + immigrants_per_year

    # new population
    new_size = size + (pop_change * years)
    return int(new_size)


# Constants
FREEZING_CONSTANT = 32


def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    celsius = (fahrenheit - FREEZING_CONSTANT) * 5/9
    return celsius

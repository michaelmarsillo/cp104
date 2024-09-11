"""
-------------------------------------------------------
[Lab 7]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""
# imports
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0

    guess = None
    while guess != number:
        guess = int(input("Enter a number greater than 1: "))
        count += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")

    print(f"You made {count} guesses.")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    while power < target:
        power *= 2
    return power


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    minimum = float('inf')
    maximum = float('-inf')
    total = 0
    count = 0

    while True:
        value = float(input("Next positive value: "))

        if value < 0:
            break

        if count == 0:
            minimum = maximum = value

        minimum = min(minimum, value)
        maximum = max(maximum, value)
        total += value
        count += 1

    average = total / count if count > 0 else 0.0

    return minimum, maximum, total, average


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    a_total = 0.0
    day = 1

    while True:
        print(f"For Day {day}")

        breakfast_cost = float(input("How much was breakfast? $:"))
        lunch_cost = float(input("How much was lunch? $:"))
        supper_cost = float(input("How much was supper? $:"))

        day_total = breakfast_cost + lunch_cost + supper_cost
        print(f"Your total for the day was ${day_total:.2f}")

        b_total += breakfast_cost
        l_total += lunch_cost
        s_total += supper_cost
        a_total += day_total

        if input("Were you away another day (Y/N)?: ") != 'Y':
            break

        day += 1

    return b_total, l_total, s_total, a_total


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    # Constants
    OVERTIME_RATE = 1.5
    TAX_RATE = 0.03625
    OVERTIME = 40

    total_net_payment = 0.0
    count = 0

    while True:
        employee_id = int(input("Employee ID: "))

        if employee_id == 0:
            break

        hourly_wage_rate = float(input("Hourly wage rate: $"))
        hours_worked = float(input("Hours worked: "))

        gross_payment = hourly_wage_rate * hours_worked
        if hours_worked > OVERTIME:
            gross_payment += (hours_worked - OVERTIME) * \
                hourly_wage_rate * (OVERTIME_RATE - 1)

        net_payment = gross_payment * (1 - TAX_RATE)

        print(f"Net payment for employee {employee_id}: ${net_payment:.2f}")

        total_net_payment += net_payment
        count += 1

    average_net_payment = total_net_payment / count if count > 0 else 0.0

    return total_net_payment, average_net_payment

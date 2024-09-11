"""
-------------------------------------------------------
[Assignment 6]
-------------------------------------------------------
Author:  Michael Marsillo
ID:      169057769
Email:   mars7769@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports


def total_wins():
    """
    -------------------------------------------------------
    Prompts the user to enter a series of strings representing the outcome of a game.
    The user can enter "purple" or "gold" as the winning team. An empty string signals the end of input.
    Returns the count of "purple" and "gold" occurrences in the input.
    Use: purple_count, gold_count = total_wins()
    -------------------------------------------------------
    Returns:
        purple_count - The count of "purple" occurrences in the input (int)
        gold_count - The count of "gold" occurrences in the input (int)
    ------------------------------------------------------
    """

    purple_count = 0
    gold_count = 0

    while True:

        user_input = input("Enter the winning team: ")

        if not user_input:
            break

        if user_input == "purple":
            purple_count += 1
        elif user_input == "gold":
            gold_count += 1

    return purple_count, gold_count


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    if number <= 1:
        prime = False
    elif number == 2:
        prime = True
    elif number % 2 == 0:
        prime = False
    else:
        divisor = 3
        while divisor * divisor <= number:
            if number % divisor == 0:
                prime = False
                break
            divisor += 2
        else:
            prime = True

    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_interest_rate = interest_rate / 100 / 12

    month = 1
    balance = principal_amount

    print("Principal:   ${:.2f}".format(principal_amount))
    print("Interest rate: {:.2f}%".format(interest_rate))
    print("Monthly payment: ${:.2f}".format(payment))
    print("----------------------------------")
    print("Month   Interest   Payment   Balance")
    print("----------------------------------")

    while balance > 0:

        monthly_interest = balance * monthly_interest_rate

        if balance - (payment - monthly_interest) < 0:
            payment = balance + monthly_interest

        balance -= (payment - monthly_interest)

        print("{:4d}   {:7.2f}   {:7.2f}   {:7.2f}".format(
            month, monthly_interest, payment, balance))

        month += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number == 0:
        digits = 1
    else:
        digits = 0

    if number < 0:
        number = abs(number)

    while number > 0:
        number //= 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    factor = 1

    while factor < number:
        if number % factor == 0:
            total += factor
        factor += 1

    return total

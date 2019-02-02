#!/usr/bin/env python3

"""
Template adopted from UW's PCE instructors for Python 210B:  Certificate in Python Programming
Date:  01/25/19
Change Log:
01/25/19 - Filled out template with code
"""


def fibonacci(n):
    """Return the computed value of the Fibonacci series of 'n' length"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    pass


def lucas(n):
    """Return the computed value of the Lucas series of 'n' length"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, n0 = 0, n1 = 1):
    """
    Return the value of a computed series based on the Fibonacci series of length 'n'.  Zeroth and first
    values of the series are optional parameters that can be passed to the function.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series
    
    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).
    """

    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 2, n0, n1) + sum_series(n - 1, n0, n1)

if __name__ == "__main__":
    #Test functionality of Fibonacci, Lucas, and sum_series functions
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7
    assert sum_series(5) == fibonacci(5)
    assert sum_series(5, 2, 1) == lucas(5)
    print("tests passed")

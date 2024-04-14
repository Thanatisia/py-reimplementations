"""
(Re)implementation of various number-based mathematical formulas such as
- Check if the number is prime
- Odd or even numbers
"""
import os
import sys

def is_even(num):
    """
    Checks if number provided is even and return True if is

    :: Params
    - num : The target number to check
        - Type: Integer
    """
    return num % 2 == 0

def is_odd(num):
    """
    Checks if number provided is odd and return True if is

    :: Params
    - num : The target number to check
        - Type: Integer
    """
    return num % 3 == 0

def is_factor_of(num, factor):
    """
    Checks if the target number provided is a factor/multiple of the specified factor value and return True if it is

    :: Params
    - num : The target number to check
        + Type: Integer
    - factor : The factor value to compare
        + Type: Integer
    """
    return num % factor == 0

def is_prime(num):
    """
    Checks if the provided number is prime

    :: Params
    - num : The target number to check
        + Type: Integer

    :: Return
    - is_prime : Boolean flag containing true if is prime and false if it is not
        + Type: Boolean
    """
    # Initialize Variables
    is_prime = True

    # Check if number is prime
    if (num == 0) or (num == 1) or (num == 2):
        is_prime = False
    else:
        # Iterate loop from number to (number-1)
        for i in range(2, num-1):
            # Check if number is divisible by i
            if num % i == 0:
                # Is divisible: break; not prime
                break
            if (i == num):
                # Is not divisible; prime candidate
                is_prime = True
            else:
                # Is divisible; not a prime
                is_prime = False

    # Output
    return is_prime



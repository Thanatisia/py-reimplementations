"""
Unit test for the submodule(s): essentials/mathematics/numbers.py
"""
import os
import sys
from essentials.mathematics.numbers import is_even, is_odd, is_factor_of, is_prime

def test_is_even(number):
    """
    Unit test: is_even() == True
    """
    assert is_even(number) == True,  "[-] Error with function is_even(): {} is even".format(number)
    print("[+] Number [{}] is even : Success".format(number))

def test_is_not_even(number):
    """
    Unit test: is_even() == False
    """
    assert is_even(number) == False, "[-] Error with function is_even(): {} is not even".format(number)
    print("[+] Number [{}] is not even : Success".format(number))

def test_is_odd(number):
    """
    Unit test: is_odd() == False
    """
    assert is_odd(number) == True,  "[-] Error with function is_odd(): {} is odd".format(number)
    print("[+] Number [{}] is odd : Success".format(number))

def test_is_not_odd(number):
    """
    Unit test: is_odd() == False
    """
    assert is_odd(number) == False, "[-] Error with function is_odd(): {} is not odd".format(number)
    print("[+] Number [{}] is not odd : Success".format(number))

def test_is_factor_of(number, factor):
    """
    Unit test: is_factor_of(number, factor) == True
    """
    assert is_factor_of(number, factor) == True, "[-] Error with function is_factor_of(): {} is a factor of {}".format(number, factor)
    print("[+] Number [{}] is a factor of [{}] : Success".format(number, factor))

def test_is_not_factor_of(number, factor):
    """
    Unit test: is_factor_of(number, factor) == False
    """
    assert is_factor_of(number, factor) == False, "[-] Error with function is_factor_of(): {} is not a factor of {}".format(number, factor)
    print("[+] Number [{}] is not a factor of [{}] : Success".format(number, factor))

def test_is_prime(number):
    """
    Unit test: is_prime(number) == True
    """
    assert is_prime(number) == True, "[-] Error with function is_prime(3)"
    print("[+] Number [{}] is prime : Success".format(number))

def test_is_not_prime(number):
    """
    Unit test: is_prime(number) == False
    """
    assert is_prime(number) == False, "[-] Error with function is_prime(2)"
    print("[+] Number [{}] is not prime : Success".format(number))

def debug():
    """
    Debug function
    """
    # Test is_even(number)
    test_is_even(2)
    test_is_not_even(3)

    # Test is_odd(number)
    test_is_odd(3)
    test_is_not_odd(2)

    # Test is_factor_of(number, factor)
    test_is_factor_of(4,2)
    test_is_not_factor_of(5,2)

    # Test is_prime(number)
    test_is_prime(3)
    test_is_not_prime(2)

if __name__ == "__main__":
    debug()


"""
Unit test for the submodule(s): essentials/mathematics/geometry.py
"""
import os
import sys
from essentials.mathematics.geometry import TwoDimensional, ThreeDimensional

def init():
    """
    Initialize global variables
    """
    global TwoD, ThreeD
    TwoD = TwoDimensional()
    ThreeD = ThreeDimensional()

def test_area_of_square(length, width, expected_answer):
    """
    Unit test: calculate_area_of_square(length, width) == expected_answer
    """
    assert TwoD.calculate_area_of_square(length, width) == expected_answer, "[-] Error with function calculate_area_of_square(length, width): Area is not the expected answer: {}".format(expected_answer)
    print("[+] Area of square of given length [{}] and width [{}] == {} : Success".format(length, width, expected_answer))

def test_area_of_triangle(base, height, expected_answer):
    """
    Unit test: calculate_area_of_triangle(base, height) == expected_answer
    """
    assert TwoD.calculate_area_of_triangle(base, height) == expected_answer, "[-] Error with function calculate_area_of_triangle(base, height): Area is not the expected answer: {}".format(expected_answer)
    print("[+] Area of triangle of given base [{}] and height [{}] == {} : Success".format(base, height, expected_answer))

def test_volume_of_cube(edge, expected_answer):
    """
    Unit test: calculate_volume_of_cube(number) == expected_answer
    """
    assert ThreeD.calculate_volume_of_cube(edge) == expected_answer, "[-] Error with function calculate_volume_of_cube(): Volume is not the expected answer: {}".format(expected_answer)
    print("[+] Volume of cube of the given edge: {} == {} : Success".format(edge, expected_answer))

def debug():
    """
    Debug function
    """
    # Test calculate_area_of_square()
    test_area_of_square(2,3,6)

    # Test calculate_area_of_triangle()
    test_area_of_triangle(2,3,3)

    # Test calculate_volume_of_cube()
    test_volume_of_cube(2, 8)

if __name__ == "__main__":
    init()
    debug()


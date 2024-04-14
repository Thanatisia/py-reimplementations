"""
(Re)implementation of various geometry mathematical formulas such as
- Formula of shapes
"""
import os
import sys
import math

class TwoDimensional():
    """
    2-Dimensional objects
    """
    def calculate_area_of_triangle(self, base, height):
        """
        Calculate the area of triangle: 1/2 * base * height
        """
        return 1/2 * base * height

    def calculate_area_of_square(self, length, width):
        """
        Calculate the area of a square: Length * Width

        :: Params
        - length: The horizontal distance of a 4-sided 2D object (Square)
            + Type: Integer
        """
        return length * width

    def calculate_circumference_of_circle(self, radius):
        """
        Calculate the circumference (outer distance) of a circle: 2 * pi * radius

        :: Params
        - radius: The radius of a circle (1/2 diameter)
            + Type: Integer
        """
        return 2 * math.pi * radius

    def calculate_area_of_circle(self, radius):
        """
        Calculate the area of a circle: pi * radius^2

        :: Params
        - radius: The radius of a circle (1/2 diameter)
            + Type: Integer
        """
        return math.pi * math.pow(radius, 2)

    def calculate_area_of_trapezium(self, base, length, height):
        """
        Calculate the area of a Trapezium (Prism): 1/2 * (length+base) * height

        :: Params
        - base: The base of the trapezium is the shorter line of the top and bottom
            + Type: Integer
        - length: The length of the trapezium is the longer line between the top and bottom
            + Type: Integer
        - height: The vertical distance between the short line and the tall line
            + Type: Integer
        """
        return 1/2 * (base + length) * height

class ThreeDimensional():
    """
    3-Dimensional objects
    """
    def calculate_area_of_cube(self, area, number_of_sides):
        """
        Calculate the 3D area of an N-sided cube object with the same length on all the surfaces:
            (length * breath) * number-of-sides = (area) * number_of_sides

        :: Params
        - area: The surface area of 1 side; where every surface has the same area
            + Type: Integer
        - number_of_sides: Specify the number of surfaces the cube has
            + Type: Integer
        """
        return area * number_of_sides

    def calculate_volume_of_cube(self, edge):
        """
        Calculate the 3D volume of an N-sided cube object with the same length on all the surfaces: edge^3

        :: Params
        - edge: The edge is the length of its sides (aka edges)
            + Type: Integer
        """
        return math.pow(edge, 3)

    def calculate_area_of_cuboid(self, length, breadth, height):
        """
        Calculate the 3D area of an N-sided cuboid: 2 * (length + breath + height)

        :: Params
        - length: The horizontal (X-axis) distance of a 4-sided 3D object (Cube)
            + Type: Integer
        - breadth: The Z-axis internal distance of a 4-sided 3D object
            + Type: Integer
        - height: The vertical (Y-axis) distance of a 4-sided 3D object
            + Type: Integer
        """
        return 2 * (length + breadth + height)

    def calculate_volume_of_cuboid(self, length, breadth, height):
        """
        Calculate the 3D volume of an N-sided cuboid : length * breath * height

        :: Params
        - length: The horizontal (X-axis) distance of a 4-sided 3D object (Cube)
            + Type: Integer
        - breadth: The Z-axis internal distance of a 4-sided 3D object
            + Type: Integer
        - height: The vertical (Y-axis) distance of a 4-sided 3D object
            + Type: Integer
        """
        return length * breadth * height

    def calculate_area_of_sphere(self, radius):
        """
        Calculate the 3D area of a sphere: 4 * pi * r^2

        :: Params
        - radius: The radius of a sphere (1/2 diameter)
            + Type: Integer
        """
        return 4 * math.pi * math.pow(radius, 2)

    def calculate_volume_of_sphere(self, radius):
        """
        Calculate the 3D volume of a sphere: 4/3 * pi * radius^3

        :: Params
        - radius: The radius of a sphere (1/2 diameter)
            + Type: Integer
        """
        return 4/3 * math.pi * math.pow(radius, 3)

    def calculate_volume_of_trapezium(self, base, length, height, depth):
        """
        Calculate the volume of a 3D Trapezoid (Prism): (1/2 * (length+base) * height) * depth

        :: Params
        - base: The base of the trapezium is the shorter line of the top and bottom
            + Type: Integer
        - length: The length of the trapezium is the longer line between the top and bottom
            + Type: Integer
        - height: The vertical distance between the short line and the tall line
            + Type: Integer
        - depth: The internal distance (Z-axis) from the short line going inwards
            + Type: Integer
        """
        return (1/2 * (base + length) * height) * depth


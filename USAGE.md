USAGE
=====

## Documentations

*Library*
---------

### Package
- essentials : The primary py-reimplementations package; A library consisting of various package dependencies and reimplementations of various essential functions in a single library/framework for various programming languages

### Modules
- essentials
    - mathematics/ : Submodule containing Mathematics formula reimplementations (If is even, odd, prime etc etc)
        + geometry.py : For Geometrical mathematic formulas
        + numbers.py : For number system-based mathematical formulas

### Classes
- essentials.mathematics.geometry
    - `.TwoDimensional()` : Initialize the class for working with functions relating to calculating 2D objects
    - `.ThreeDimensional()` : Initialize the class for working with functions relating to calculating 3D objects

### Functions
- essentials.mathematics.geometry.TwoDimensional()
    - `.calculate_area_of_triangle(base, height)`: Calculate the area of triangle: 1/2 * base * height
        - Parameter/Argument Signature
            - base: The base (horizontal distance) of the triangle
                + Type: Integer
            - height: The vertical distance of the triangle
                + Type: Integer
        - Return
            - area: The total surface area of the triangle given the base and height
                + Type: Integer

    - `.calculate_area_of_square(length, width)`: Calculate the area of a square: Length * Width
        - Parameter/Argument Signature
            - length: The horizontal distance of a 4-sided 2D object (Square)
                + Type: Integer
        - Return
            - area: The total surface area of the square given the length and width
                + Type: Integer

    - `.calculate_circumference_of_circle(radius)`: Calculate the circumference (outer distance) of a circle: 2 * pi * radius
        - Parameter/Argument Signature
            - radius: The radius of a circle (1/2 diameter)
                + Type: Integer
        - Return
            - circumference: The overall distance surrounding the circle
                + Type: Integer

    - `.calculate_area_of_circle(radius)`: Calculate the area of a circle: pi * radius^2
        - Parameter/Argument Signature
            - radius: The radius of a circle (1/2 diameter)
                + Type: Integer
        - Return
            - area: The total surface area of the circle
                + Type: Integer

    - `.calculate_area_of_trapezium(base, length, height)`: Calculate the area of a Trapezium (Prism): 1/2 * (length+base) * height
        - Parameter/Argument Signature
            - base: The base of the trapezium is the shorter line of the top and bottom
                + Type: Integer
            - length: The length of the trapezium is the longer line between the top and bottom
                + Type: Integer
            - height: The vertical distance between the short line and the tall line
                + Type: Integer
        - Return
            - area: The total surface area of the trapezium
                + Type: Integer


- essentials.mathematics.geometry.ThreeDimensional()
    - `.calculate_area_of_cube(area, number_of_sides)`: Calculate the 3D area of an N-sided cube object with the same length on all the surfaces
        - Parameter/Argument Signature
            - area: The surface area of 1 side; where every surface has the same area
                + Type: Float
            - number_of_sides: Specify the number of surfaces the cube has
                + Type: Integer
        - Return
            - area: The total surface area of a 3-dimensional cube
                + Type: Float

    - `.calculate_volume_of_cube(edge)`: Calculate the 3D volume of an N-sided cube object with the same length on all the surfaces
        - Parameter/Argument Signature
            - edge: The edge is the length of its sides (aka edges)
                + Type: Integer
        - Return
            - volume: The total volume/space the cube can hold
                + Type: Float

    - `.calculate_area_of_cuboid(length, breadth, height)`: Calculate the 3D area of an N-sided cuboid
        - Parameter/Argument Signature
            - length: The horizontal (X-axis) distance of a 4-sided 3D object (Cube)
                + Type: Float
            - breadth: The Z-axis internal distance of a 4-sided 3D object
                + Type: Float
            - height: The vertical (Y-axis) distance of a 4-sided 3D object
                + Type: Float
        - Return
            - area: The total surface area of a 3-dimensional cuboid
                + Type: Float

    - `.calculate_volume_of_cuboid(length, breadth, height)`: Calculate the 3D volume of an N-sided cuboid
        - Parameter/Argument Signature  
            - length: The horizontal (X-axis) distance of a 4-sided 3D object (Cube)
                + Type: Float
            - breadth: The Z-axis internal distance of a 4-sided 3D object
                + Type: Float
            - height: The vertical (Y-axis) distance of a 4-sided 3D object
                + Type: Float
        - Return
            - volume: The total volume/space the cuboid can hold
                + Type: Float

    - `.calculate_area_of_sphere(radius)`: Calculate the 3D area of a sphere
        - Parameter/Argument Signature
            - radius: The radius of a sphere (1/2 diameter)
                + Type: Float
        - Return
            - area: The total surface area of a 3-dimensional sphere
                + Type: Float

    - `.calculate_volume_of_sphere(radius)`: Calculate the 3D volume of a sphere
        - Parameter/Argument Signature
            - radius: The radius of a sphere (1/2 diameter)
                + Type: Float
        - Return
            - volume: The total volume/space the sphere can hold
                + Type: Float

    - `.calculate_volume_of_trapezium(base, length, height, depth)`: Calculate the volume of a 3D Trapezoid (Prism)
        - Parameter/Argument Signature
            - base: The base of the trapezium is the shorter line of the top and bottom
                + Type: Float
            - length: The length of the trapezium is the longer line between the top and bottom
                + Type: Float
            - height: The vertical distance between the short line and the tall line
                + Type: Float
            - depth: The internal distance (Z-axis) from the short line going inwards
                + Type: Float
        - Return
            - volume: The total volume/space the trapezoid prism can hold
                + Type: Float

- essentials.mathematics.numbers
    - `.is_even(num)`: Checks if number provided is even and return True if is even
        - Parameter/Argument Signature
            - num : The target number to check
                + Type: Integer
        - Return
            - flag : Boolean value determining if the number is even (True) or not even (False)
                + Type: Boolean

    - `.is_odd(num)`: Checks if number provided is odd and return True if is odd
        - Parameter/Argument Signature
            - num : The target number to check
                + Type: Integer
        - Return
            - flag : Boolean value determining if the number is odd (True) or not odd (False)
                + Type: Boolean

    - `.is_factor_of(num, factor)`: Checks if the target number provided is a factor/multiple of the specified factor value and return True if it is
        - Parameter/Argument Signature
            - num : The target number to check
                + Type: Integer
            - factor : The factor value to compare
                + Type: Integer
        - Return
            - flag : Boolean value determining if the number is/is not a factor of the provided factor value
                + Type: Boolean

    - `.is_prime(num)`: Checks if the provided number is prime
        - Parameter/Argument Signature
            - num : The target number to check
                + Type: Integer
        - Return
            - flag : Boolean value determining if the number is/is not prime
                + Type: Boolean

### Data Classes/Types

### Attributes/Variables Objects

*Usage*
-------
- Import python package
    - mathematics formulas
        ```python
        from essentials.mathematics.[topic] import functions|classes
        ```

- Initialize Variables
    ```python
    # Initialize Variables
    ```

- Initialize Module Classes


## Wiki

## Resources

## References

## Remarks

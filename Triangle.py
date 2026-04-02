#Enhanced version of Triangle.py
# -*- coding: utf-8 -*-

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the triangle satisfies the Pythagorean theorem, return 'Right'
    """

    # verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be > 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # equilateral
    if a == b and b == c:
        return 'Equilateral'

    # right triangle
    sides = sorted([a, b, c])
    if (sides[0] ** 2) + (sides[1] ** 2) == (sides[2] ** 2):
        return 'Right'

    # scalene
    if (a != b) and (b != c) and (a != c):
        return 'Scalene'

    # otherwise isoceles
    return 'Isoceles'

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of squares of any two sides equals the square of the third side,
        return 'Right'
    """

    # Verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Require that the input values be > 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # BUG FIX 1: original had `b <= b` (always True); corrected to `b <= 0`
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # BUG FIX 2: original triangle-inequality check was completely wrong.
    # The sum of any two sides must be STRICTLY GREATER than the third side.
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return 'NotATriangle'

    # Now we know we have a valid triangle.

    # BUG FIX 3: original equilateral check was `a == b and b == a` (missing c).
    if a == b and b == c:
        return 'Equilateral'

    # BUG FIX 4: original right-triangle check used multiplication (a*2) instead
    # of exponentiation (a**2), and only checked one combination.
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'

    # BUG FIX 5: original scalene check had `a != b` twice (should end with `a != c`).
    if a != b and b != c and a != c:
        return 'Scalene'

    return 'Isoceles'

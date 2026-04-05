# -*- coding: utf-8 -*-
"""
TestTriangle.py — Comprehensive unit tests for classifyTriangle()

@author: student
"""

import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    # ----------------------------- Right triangles -----------------------------
    def testRightTriangle_3_4_5(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangle_5_3_4(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangle_4_3_5(self):
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right', '4,3,5 is a Right triangle')

    def testRightTriangle_5_12_13(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def testRightTriangle_8_15_17(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 is a Right triangle')

    def testRightTriangle_6_8_10(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    # ----------------------------- Equilateral triangles -----------------------
    def testEquilateral_1_1_1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')

    def testEquilateral_10_10_10(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be Equilateral')

    def testEquilateral_100_100_100(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100,100,100 should be Equilateral')

    # ----------------------------- Isosceles triangles -------------------------
    def testIsosceles_2_2_3(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be Isoceles')

    def testIsosceles_5_5_8(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles', '5,5,8 should be Isoceles')

    def testIsosceles_3_5_5(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles', '3,5,5 should be Isoceles')

    def testIsosceles_5_3_5(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles', '5,3,5 should be Isoceles')

    # ----------------------------- Scalene triangles ---------------------------
    def testScalene_3_4_6(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 should be Scalene')

    def testScalene_7_10_12(self):
        self.assertEqual(classifyTriangle(7, 10, 12), 'Scalene', '7,10,12 should be Scalene')

    def testScalene_5_7_9(self):
        self.assertEqual(classifyTriangle(5, 7, 9), 'Scalene', '5,7,9 should be Scalene')

    # ----------------------------- Not a triangle ------------------------------
    def testNotATriangle_1_2_3(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')

    def testNotATriangle_1_1_3(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle')

    def testNotATriangle_10_1_1(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 is not a triangle')

    def testNotATriangle_5_1_2(self):
        self.assertEqual(classifyTriangle(5, 1, 2), 'NotATriangle', '5,1,2 is not a triangle')

    # ----------------------------- Invalid inputs ------------------------------
    def testInvalid_zero(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 should be InvalidInput')

    def testInvalid_negative(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput', '-1,4,5 should be InvalidInput')

    def testInvalid_b_zero(self):
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput', '1,0,1 should be InvalidInput')

    def testInvalid_c_zero(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1,1,0 should be InvalidInput')

    def testInvalid_over200_a(self):
        self.assertEqual(classifyTriangle(201, 1, 1), 'InvalidInput', '201,1,1 should be InvalidInput')

    def testInvalid_over200_b(self):
        self.assertEqual(classifyTriangle(1, 201, 1), 'InvalidInput', '1,201,1 should be InvalidInput')

    def testInvalid_over200_c(self):
        self.assertEqual(classifyTriangle(1, 1, 201), 'InvalidInput', '1,1,201 should be InvalidInput')

    def testInvalid_float(self):
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput', '1.5,2,3 should be InvalidInput')

    def testInvalid_string(self):
        self.assertEqual(classifyTriangle('a', 2, 3), 'InvalidInput', 'a,2,3 should be InvalidInput')

    # ----------------------------- Edge cases ----------------------------------
    def testEdge_max_valid(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be Equilateral')

    def testEdge_two_sides_sum_equals_third(self):
        # Degenerate: a + b == c is NOT a valid triangle
        self.assertEqual(classifyTriangle(3, 5, 8), 'NotATriangle', '3,5,8 should be NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

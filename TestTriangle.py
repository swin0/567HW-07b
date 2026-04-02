#Enhanced TestTriangle.py
# -*- coding: utf-8 -*-
import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # Right triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right')

    # Equilateral
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def testEquilateralLarger(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral')

    # Isoceles
    def testIsocelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')

    def testIsocelesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')

    def testIsocelesC(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    # Scalene
    def testScaleneA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene')

    # Not a triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(2, 2, 4), 'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle')

    # Invalid input: zero / negative
    def testInvalidZeroA(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testInvalidZeroB(self):
        self.assertEqual(classifyTriangle(4, 0, 5), 'InvalidInput')

    def testInvalidZeroC(self):
        self.assertEqual(classifyTriangle(4, 5, 0), 'InvalidInput')

    def testInvalidNegative(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput')

    # Invalid input: too large
    def testInvalidTooLargeA(self):
        self.assertEqual(classifyTriangle(201, 4, 5), 'InvalidInput')

    def testInvalidTooLargeB(self):
        self.assertEqual(classifyTriangle(4, 201, 5), 'InvalidInput')

    def testInvalidTooLargeC(self):
        self.assertEqual(classifyTriangle(4, 5, 201), 'InvalidInput')

    # Invalid input: non-integer
    def testInvalidFloat(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    def testInvalidString(self):
        self.assertEqual(classifyTriangle("3", 4, 5), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

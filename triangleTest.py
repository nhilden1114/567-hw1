'''
Created on Aug 29, 2018

@author: Nicole Hilden
I pledge my honor that I have abided by the Stevens Honor System
'''

import unittest
from hw1.triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    
    def test_scalene(self):
        """ Test aspects of a scalene triangle """
        self.assertEqual(classify_triangle(3,4,5),'Your triangle is scalene and right', '3,4,5 is scalene and right')
        self.assertEqual(classify_triangle(5,3,4),'Your triangle is scalene and right', '5,3,4 is scalene and right')
        self.assertEqual(classify_triangle(3,7,9),'Your triangle is scalene and not right', '3,7,9 is scalene and not right')
        self.assertEqual(classify_triangle(5,10,15),'Not a triangle', '5,10,15 is not a triangle')
        self.assertNotEqual(classify_triangle(2, 2, 2), 'Your triangle is scalene and right', '2,2,2 is equilateral and not right')
        self.assertNotEqual(classify_triangle(4, 4, 6), 'Your triangle is scalene and right', '4,4,6 is isoceles and not right')
        self.assertNotEqual(classify_triangle(2, 4, 12), 'Your triangle is scalene and right', '2,4,12 is not a triangle')

    def test_equilateral(self):
        """ Test aspects of an equilateral triangle """
        self.assertEqual(classify_triangle(3,3,3),'Your triangle is equilateral and not right', '3,3,3 is equilateral and not right')
        self.assertEqual(classify_triangle(5,5,5),'Your triangle is equilateral and not right', '5,5,5 is equilateral and not right')
        self.assertEqual(classify_triangle(9,9,9),'Your triangle is equilateral and not right', '9,9,9 is equilateral and not right')
        self.assertEqual(classify_triangle(0,0,0),'Not a triangle', '0,0,0 is not a triangle')
        self.assertNotEqual(classify_triangle(3,4,5), 'Your triangle is equilateral and not right', '2,3,4 is scalene and right')
        self.assertNotEqual(classify_triangle(4,4,6), 'Your triangle is equilateral and right', '4,4,6 is isosceles and not right')
        self.assertNotEqual(classify_triangle(1,1,1), 'Your triangle is equilateral and right', '1,1,1 is equilateral and not right')

    def test_isosceles(self):
        """ Test aspects of an isosceles triangle """
        self.assertEqual(classify_triangle(3,3,4),'Your triangle is isosceles and not right', '3,3,4 is isosceles and not right')
        self.assertEqual(classify_triangle(5,5,7),'Your triangle is isosceles and not right', '5,5,7 is isosceles and not right')
        self.assertEqual(classify_triangle(10,10,14),'Your triangle is isosceles and not right', '10,10,14 is isosceles and not right')
        self.assertEqual(classify_triangle(2,2,6),'Not a triangle', '2,2,6 is not a triangle')
        self.assertNotEqual(classify_triangle(2,2,2), 'Your triangle is isosceles and right', '2,2,2 is equilateral and not right')
        self.assertNotEqual(classify_triangle(4,4,6), 'Your triangle is isosceles and right', '4,4,6 is isoceles and not right')
        self.assertNotEqual(classify_triangle(5,6,9), 'Your triangle is isosceles and right', '5,6,9 is scalene and not right')

    def test_notTriangle(self):
        """ Test numbers that do not make a triangle """
        self.assertEqual(classify_triangle(2,4,10), 'Not a triangle', '2,4,10 is not a triangle')
        self.assertEqual(classify_triangle(2,2,7), 'Not a triangle', '2,2,7 is not a triangle')
        self.assertEqual(classify_triangle(3,6,9), 'Not a triangle', '3,6,9 is not a triangle')
        self.assertNotEqual(classify_triangle(4,4,7), 'Not a triangle', '4,4,7 is isosceles and not right')
        self.assertNotEqual(classify_triangle(6,8,10), 'Not a triangle', '6,8,10 is scalene and right')
        self.assertNotEqual(classify_triangle(4,4,4), 'Not a triangle', '4,4,4 is equilateral and not right')
        
    def test_otherInput(self):
        """ Test inputs that are not integers """
        self.assertEqual(classify_triangle('one', 'three', 'three'), 'All values must be integers')
        self.assertEqual(classify_triangle(1, 'three', 'three'), 'All values must be integers')
        self.assertEqual(classify_triangle(1, 3, True), 'All values must be integers')
        self.assertEqual(classify_triangle(1.34557887653, 5, 3), 'All values must be integers')
        
    def test_rightTriangle(self):
        """ Test functionality of whether or not a triangle is right"""
        self.assertEqual(classify_triangle(3,4,5),'Your triangle is scalene and right', '3,4,5 is scalene and right')
        self.assertEqual(classify_triangle(6,8,10),'Your triangle is scalene and right', '6,8,10 is scalene and right')
        self.assertNotEqual(classify_triangle(3,7,9),'Your triangle is scalene and right', '3,7,9 is scalene and not right')
        self.assertNotEqual(classify_triangle(5,5,7),'Your triangle is isosceles and right', '5,5,7 is isosceles and not right')

        
if __name__ == "__main__":
    unittest.main()

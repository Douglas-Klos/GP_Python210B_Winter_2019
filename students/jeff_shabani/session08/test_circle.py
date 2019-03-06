#!/usr/bin/env python3

import io
import math
import pytest
import unittest

from Circle import *




class circleTests(unittest.TestCase):



    def test_init(self):
        """test for instantiation"""
        c = Circle(5)
        self.assertEqual(c.radius, 5)
        del c

    def test_diameter_calc(self):
        c = Circle(4)
        self.assertEqual(c.diameter, c.radius*2)
        del c

    def test_diameter_setter(self):
        c=Circle(5)
        self.assertEqual(c.diameter, 10)
        c.diameter = 24
        self.assertEqual(c.diameter, 24)
        self.assertEqual(c.radius, 12)
        del c

    def test_area(self):
        c = Circle(5)
        self.assertEqual(c.area, math.pi * pow(c.radius,2))

if __name__ == '__main__':
    unittest.main()
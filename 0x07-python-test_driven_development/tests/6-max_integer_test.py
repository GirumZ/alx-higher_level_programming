#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ A class for unittesting max_integer function"""

    def test_max_integer(self):
        """ A test for the max_integer function"""

        self.assertEqual(max_integer([4,6,-1,0]), 6)
        self.assertEqual(max_integer([2,2,2,2]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-2,-6,-14,-3]), -2)

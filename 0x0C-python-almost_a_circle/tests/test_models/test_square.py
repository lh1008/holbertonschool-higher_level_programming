#!/usr/bin/python3
"""Module for unittest cases"""
import unittest


from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """Class unittest for Base"""

    def test_area(self):
        """Test area square"""
        sq = Square(2)
        self.assertEqual(sq.area(), 4)
        del sq

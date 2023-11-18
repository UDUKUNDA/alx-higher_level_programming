#!/usr/bin/python3
""" The tests for square """

import unittest

from models.square import Square



class TestSquare(unittest.TestCase):

    def test_initialization_success(self):

        sq1 = Square(5)

        sq2 = Square(10)

        self.assertEqual(sq1.id, 5)

        self.assertEqual(sq2.id, 6)


    def test_initialization_without_arguments(self):


        self.assertRaises(TypeError, Square)


if __name__ == '__main__':

    unittest.main()

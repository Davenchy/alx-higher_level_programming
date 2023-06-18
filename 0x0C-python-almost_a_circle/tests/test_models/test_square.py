#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareCase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docs_and_attributes(self):
        self.assertTrue(hasattr(Square, '__doc__'))
        self.assertTrue(hasattr(Square.__init__, '__doc__'))

        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_init_values_and_to_string(self):
        s = Square(5, 20, 30, 10)

        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.id, 10)
        self.assertEqual(str(s), '[Square] (10) 20/30 - 5')

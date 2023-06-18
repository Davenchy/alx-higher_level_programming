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

    def test_size(self):
        s = Square(10)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 10')

        s.size = 50
        self.assertEqual(str(s), '[Square] (1) 0/0 - 50')

        with self.assertRaises(ValueError) as err:
            s.size = 0
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            s.size = -1
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(TypeError) as err:
            s.size = "10"
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_update(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')

        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')

        s1.update(1, 2)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 2')

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), '[Square] (1) 3/0 - 2')

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')

        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/4 - 2')

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), '[Square] (1) 12/1 - 7')

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), '[Square] (89) 12/1 - 7')

        s1.update(width=7, height=89)
        self.assertEqual(str(s1), '[Square] (89) 12/1 - 7')

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleCase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docs_and_attributes(self):
        self.assertTrue(hasattr(Rectangle, '__doc__'))
        self.assertTrue(hasattr(Rectangle.__init__, '__doc__'))

        r = Rectangle(0, 0)
        self.assertIsInstance(r, Base)
        self.assertTrue(hasattr(r, '_Rectangle__width'))
        self.assertTrue(hasattr(r, '_Rectangle__height'))
        self.assertTrue(hasattr(r, '_Rectangle__x'))
        self.assertTrue(hasattr(r, '_Rectangle__y'))
        self.assertTrue(hasattr(r, 'id'))

    def test_width(self):
        r = Rectangle(1, 0)
        self.assertEqual(r._Rectangle__width, 1)

        r = Rectangle(10, 0)
        self.assertEqual(r.width, 10)

        self.assertRaises(ValueError, Rectangle, -1, 0)
        self.assertRaises(TypeError, Rectangle, "invalid", 0)

    def test_height(self):
        r = Rectangle(0, 1)
        self.assertEqual(r._Rectangle__height, 1)

        r = Rectangle(0, 10)
        self.assertEqual(r.height, 10)

        self.assertRaises(ValueError, Rectangle, 0, -1)
        self.assertRaises(TypeError, Rectangle, 0, "invalid")

    def test_x(self):
        r = Rectangle(1, 0)
        self.assertEqual(r._Rectangle__x, 0)

        r = Rectangle(1, 0, 5)
        self.assertEqual(r._Rectangle__x, 5)

        r = Rectangle(10, 0, 10)
        self.assertEqual(r.x, 10)

        self.assertRaises(TypeError, Rectangle, 0, 0, "invalid")

    def test_y(self):
        r = Rectangle(0, 1)
        self.assertEqual(r._Rectangle__y, 0)

        r = Rectangle(0, 1, 0, 5)
        self.assertEqual(r._Rectangle__y, 5)

        r = Rectangle(0, 10, 10, 15)
        self.assertEqual(r.y, 15)

        self.assertRaises(TypeError, Rectangle, 0, 0, 0, "invalid")

    def test_id(self):
        r = Rectangle(0, 0)
        self.assertEqual(r.id, 1)

        r = Rectangle(0, 0, 0, 0)
        self.assertEqual(r.id, 2)

        r = Rectangle(0, 0, 0, 0, 15)
        self.assertEqual(r.id, 15)
        self.assertEqual(Base._Base__nb_objects, 2)

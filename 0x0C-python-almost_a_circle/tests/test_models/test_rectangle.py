import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleCase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docs_and_attributes(self):
        self.assertTrue(hasattr(Rectangle, '__doc__'))
        self.assertTrue(hasattr(Rectangle.__init__, '__doc__'))

        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)
        self.assertTrue(hasattr(r, '_Rectangle__width'))
        self.assertTrue(hasattr(r, '_Rectangle__height'))
        self.assertTrue(hasattr(r, '_Rectangle__x'))
        self.assertTrue(hasattr(r, '_Rectangle__y'))
        self.assertTrue(hasattr(r, 'id'))

    def test_width(self):
        r = Rectangle(1, 2)
        self.assertEqual(r._Rectangle__width, 1)

        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

        with self.assertRaises(ValueError) as err:
            Rectangle(-1, 0)
        self.assertEqual(str(err.exception), "width must be > 0")
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 0)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(TypeError) as err:
            Rectangle("invalid", 0)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_height(self):
        r = Rectangle(1, 2)
        self.assertEqual(r._Rectangle__height, 2)

        r = Rectangle(1, 10)
        self.assertEqual(r.height, 10)

        with self.assertRaises(ValueError) as err:
            Rectangle(1, -1)
        self.assertEqual(str(err.exception), "height must be > 0")
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 0)
        self.assertEqual(str(err.exception), "height must be > 0")

        with self.assertRaises(TypeError) as err:
            Rectangle(1, "invalid")
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_x(self):
        r = Rectangle(1, 2)
        self.assertEqual(r._Rectangle__x, 0)

        r = Rectangle(1, 2, 5)
        self.assertEqual(r._Rectangle__x, 5)

        r = Rectangle(1, 2, 5)
        self.assertEqual(r.x, 5)

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, "invalid")
        self.assertEqual(str(err.exception), "x must be an integer")

        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, -1)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_y(self):
        r = Rectangle(1, 2)
        self.assertEqual(r._Rectangle__y, 0)

        r = Rectangle(1, 2, 0, 5)
        self.assertEqual(r._Rectangle__y, 5)

        r = Rectangle(1, 2, 10, 15)
        self.assertEqual(r.y, 15)

        with self.assertRaises(TypeError) as err:
            Rectangle(1, 1, 0, "invalid")
        self.assertEqual(str(err.exception), "y must be an integer")

        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, 0, -1)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_id(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)

        r = Rectangle(1, 2, 0, 0)
        self.assertEqual(r.id, 2)

        r = Rectangle(1, 2, 0, 0, 15)
        self.assertEqual(r.id, 15)
        self.assertEqual(Base._Base__nb_objects, 2)

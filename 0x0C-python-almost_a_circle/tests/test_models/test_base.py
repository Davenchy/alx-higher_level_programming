import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def test_docs(self):
        self.assertTrue(hasattr(Base, '__doc__'))
        self.assertTrue(hasattr(Base.__init__, '__doc__'))

    def test_auto_manual_id(self):
        self.assertEqual(Base._Base__nb_objects, 0)

        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

        b = Base()
        self.assertEqual(b.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

        b = Base(50)
        self.assertEqual(b.id, 50)
        self.assertEqual(Base._Base__nb_objects, 2)

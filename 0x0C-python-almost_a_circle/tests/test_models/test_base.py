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

    def test_to_json_string(self):
        self.assertTrue(hasattr(Base, 'to_json_string'))

        data = None
        self.assertEqual(Base.to_json_string(data), '[]')

        data = []
        self.assertEqual(Base.to_json_string(data), '[]')

        data = [{'name': 'Davenchy', 'age': 24}]
        self.assertEqual(Base.to_json_string(data),
                         '[{"name": "Davenchy", "age": 24}]')

        data = "hello"
        self.assertRaises(TypeError, Base.to_json_string, data)

        data = ["hello"]
        self.assertRaises(TypeError, Base.to_json_string, data)

    def test_from_json_string(self):
        self.assertTrue(hasattr(Base, 'from_json_string'))

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("hello world"), [])
        self.assertEqual(Base.from_json_string('[{"x": 5}]'), [{"x": 5}])

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(max_integer())

    def test_one_number(self):
        self.assertEqual(max_integer([1]), 1)

    def test_many_numbers(self):
        self.assertEqual(max_integer([12, 3, 4, 5, 6]), 12)
        self.assertEqual(max_integer([i for i in range(1000)]), 999)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-12, -3, -4]), -3)
        self.assertEqual(max_integer([-12, -3, -4, 6]), 6)

    def test_none_ints(self):
        self.assertEqual(max_integer(["fadi", "davenchy"]), "fadi")
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([5.9, 3.2]), 5.9)

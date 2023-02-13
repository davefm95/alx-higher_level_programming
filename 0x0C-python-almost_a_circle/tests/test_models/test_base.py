#!/usr/bin/python3
"""Test modeule for base class"""
import sys
sys.path.append("...")
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """The test class"""
    def setUp(self):
        """Sets up cls vats"""
        Base.__nb_objects = 0

    def test_base(self):
        """Test function"""
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(1, b.id)
        b = Base(12)
        self.assertEqual(12, b.id)
        self.assertIsInstance(b, Base)
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(2, b.id)

if __name__ == "__main__":
    unittest.main()

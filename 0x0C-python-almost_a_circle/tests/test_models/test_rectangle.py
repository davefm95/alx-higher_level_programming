#!/usr/bin/python3
import sys
sys.path.append("...")
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_rect(self):
        r = Rectangle(2, 3, 1, 4, 101)
        self.assertEqual(2, r.width)
        self.assertEqual(3, r.height)
        self.assertEqual(1, r.x)
        self.assertEqual(4, r.y)
        self.assertEqual(101, r.id)
        with  self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "str"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "str"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = "str"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = "str"
        with  self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -1
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -1

if __name__ == "__main__":
    unittest.main()

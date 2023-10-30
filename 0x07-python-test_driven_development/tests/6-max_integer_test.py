i#!/usr/bin/python3
"""The Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The unittest class for max_integer"""
    def test_module_docstring(self):
        """The Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """The Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """The Tests for Teh empty list []"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """The Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """The Tests for only one number in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """The Tests for all positive with max at end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_positive_middle(self):
        """The Tests for all positive with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_positive_beginning(self):
        """The Tests for all positive with max at beginning"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)

    def test_one_negative(self):
        """The Tests for list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """The Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """The Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """The Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()

import unittest
from utils import validate_input

class TestUtils(unittest.TestCase):
    def test_validate_input_valid_int(self):
        result = validate_input("123", int)
        self.assertEqual(result, 123)

    def test_validate_input_invalid_int(self):
        result = validate_input("abc", int)
        self.assertIsNone(result)

    def test_validate_input_valid_float(self):
        result = validate_input("12.34", float)
        self.assertEqual(result, 12.34)

    def test_validate_input_invalid_float(self):
        result = validate_input("abc", float)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
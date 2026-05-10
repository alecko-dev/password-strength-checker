import unittest
import math
import string

from analysis import (
    analyse_character_classes,
    calculate_pool_size,
    calculate_entropy,
)


class TestAnalysis(unittest.TestCase):

    def test_lowercase_detection(self):
        result = analyse_character_classes("abc")

        self.assertTrue(result["has_lowercase"])
        self.assertFalse(result["has_uppercase"])
        self.assertFalse(result["has_number"])
        self.assertFalse(result["has_symbol"])

    def test_uppercase_and_digit_detection(self):
        result = analyse_character_classes("ABC123")

        self.assertFalse(result["has_lowercase"])
        self.assertTrue(result["has_uppercase"])
        self.assertTrue(result["has_number"])
        self.assertFalse(result["has_symbol"])

    def test_symbol_detection(self):
        result = analyse_character_classes("hello!")

        self.assertTrue(result["has_lowercase"])
        self.assertTrue(result["has_symbol"])

    def test_lowercase_pool_size(self):
        character_classes = analyse_character_classes("abc")
        pool_size = calculate_pool_size(character_classes)

        self.assertEqual(pool_size, 26)

    def test_mixed_pool_size(self):
        character_classes = analyse_character_classes("Abc123!")
        pool_size = calculate_pool_size(character_classes)

        self.assertEqual(pool_size, 94)

    def test_empty_password_entropy_is_zero(self):
        entropy = calculate_entropy("", 26)

        self.assertEqual(entropy, 0)

    def test_entropy_calculation(self):
        entropy = calculate_entropy("abc", 26)
        expected = 3 * math.log2(26)

        self.assertAlmostEqual(entropy, expected)

    def test_mixed_case_has_higher_entropy_than_lowercase_same_length(self):
        lowercase_classes = analyse_character_classes("abcdef")
        mixed_classes = analyse_character_classes("AbCdEf")

        lowercase_pool = calculate_pool_size(lowercase_classes)
        mixed_pool = calculate_pool_size(mixed_classes)

        lowercase_entropy = calculate_entropy("abcdef", lowercase_pool)
        mixed_entropy = calculate_entropy("AbCdEf", mixed_pool)

        self.assertGreater(mixed_entropy, lowercase_entropy)


if __name__ == "__main__":
    unittest.main()
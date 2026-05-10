import unittest

from verdict import determine_strength


def make_results(entropy=70, is_common=False, breach_count=0, has_repeats=False):
    return {
        "entropy": entropy,
        "is_common": is_common,
        "breach_count": breach_count,
        "has_repeats": has_repeats,
    }


class TestVerdict(unittest.TestCase):

    def test_breached_password_is_compromised(self):
        results = make_results(entropy=100, breach_count=1000)

        self.assertEqual(determine_strength(results), "Compromised")

    def test_common_password_is_very_weak(self):
        results = make_results(entropy=100, is_common=True)

        self.assertEqual(determine_strength(results), "Very Weak")

    def test_very_weak_entropy(self):
        results = make_results(entropy=20)

        self.assertEqual(determine_strength(results), "Very Weak")

def test_entropy_boundary_at_28(self):
    self.assertEqual(determine_strength(make_results(entropy=27.99)), "Very Weak")
    self.assertEqual(determine_strength(make_results(entropy=28)), "Weak")

    def test_medium_entropy_boundary(self):
        results = make_results(entropy=36)

        self.assertEqual(determine_strength(results), "Medium")

    def test_strong_entropy_boundary(self):
        results = make_results(entropy=60)

        self.assertEqual(determine_strength(results), "Strong")

    def test_very_strong_entropy_boundary(self):
        results = make_results(entropy=80)

        self.assertEqual(determine_strength(results), "Very Strong")


if __name__ == "__main__":
    unittest.main()
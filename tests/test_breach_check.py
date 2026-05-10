import unittest
import urllib.error
from unittest.mock import patch, Mock

from breach_check import (
    hash_password_sha1,
    split_hash_for_hibp,
    check_breach_count,
)


class TestBreachCheck(unittest.TestCase):

    def test_sha1_hash_for_password(self):
        sha1_hash = hash_password_sha1("password")

        self.assertEqual(
            sha1_hash,
            "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8"
        )

    def test_split_hash_for_hibp(self):
        sha1_hash = "5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8"
        prefix, suffix = split_hash_for_hibp(sha1_hash)

        self.assertEqual(prefix, "5BAA6")
        self.assertEqual(suffix, "1E4C9B93F3F0682250B6CF8331B7EE68FD8")

    @patch("breach_check.urllib.request.urlopen")
    def test_check_breach_count_found(self, mock_urlopen):
        fake_response_text = (
            "00000000000000000000000000000000000:1\r\n"
            "1E4C9B93F3F0682250B6CF8331B7EE68FD8:52256179\r\n"
        )

        mock_response = Mock()
        mock_response.read.return_value = fake_response_text.encode("utf-8")
        mock_response.__enter__ = Mock(return_value=mock_response)
        mock_response.__exit__ = Mock(return_value=None)

        mock_urlopen.return_value = mock_response

        breach_count = check_breach_count("password")

        self.assertEqual(breach_count, 52256179)

    @patch("breach_check.urllib.request.urlopen")
    def test_check_breach_count_not_found(self, mock_urlopen):
        fake_response_text = (
            "00000000000000000000000000000000000:1\r\n"
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:2\r\n"
        )

        mock_response = Mock()
        mock_response.read.return_value = fake_response_text.encode("utf-8")
        mock_response.__enter__ = Mock(return_value=mock_response)
        mock_response.__exit__ = Mock(return_value=None)

        mock_urlopen.return_value = mock_response

        breach_count = check_breach_count("password")

        self.assertEqual(breach_count, 0)

    @patch("breach_check.urllib.request.urlopen")
    def test_check_breach_count_network_error_returns_none(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Network down")

        breach_count = check_breach_count("password")

        self.assertIsNone(breach_count)


if __name__ == "__main__":
    unittest.main()
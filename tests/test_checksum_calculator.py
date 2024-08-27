import unittest
from src.checksum.checksum_calculator import calculate_checksum

class TestChecksumCalculator(unittest.TestCase):

    def test_calculate_checksum(self):
        box_ids = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"
        ]
        expected_checksum = 12
        checksum = calculate_checksum(box_ids)
        self.assertEqual(checksum, expected_checksum, f"Expected checksum {expected_checksum}, but got {checksum}. Box IDs: {box_ids}")

if __name__ == '__main__':
    unittest.main()

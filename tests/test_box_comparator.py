import unittest
from src.checksum.box_comparator import find_similar_boxes, common_letters, differ_by_one

class TestBoxComparator(unittest.TestCase):

    def test_find_similar_boxes(self):
        box_ids = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"
        ]
        id1, id2 = find_similar_boxes(box_ids)
        self.assertEqual(id1, "fghij")
        self.assertEqual(id2, "fguij")

    def test_differ_by_one(self):
        self.assertTrue(differ_by_one("abcde", "axcde"))
        self.assertFalse(differ_by_one("abcde", "axcye"))

    def test_common_letters(self):
        id1 = "fghij"
        id2 = "fguij"
        common = common_letters(id1, id2)
        self.assertEqual(common, "fgij")

if __name__ == '__main__':
    unittest.main()

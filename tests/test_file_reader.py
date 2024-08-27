import unittest
from src.checksum.file_reader import read_input_file

class TestFileReader(unittest.TestCase):

    def test_read_input_file(self):
        try:
            box_ids = read_input_file('resources/input.txt')
            self.assertIsInstance(box_ids, list, "The file did not return a list.")
            self.assertGreater(len(box_ids), 0, "The list of box IDs is empty.")
        except FileNotFoundError:
            self.fail("The file 'input.txt' was not found.")
        except Exception as e:
            self.fail(f"An error occurred while reading the file: {e}")

if __name__ == '__main__':
    unittest.main()

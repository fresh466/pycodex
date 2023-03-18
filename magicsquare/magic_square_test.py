import unittest
import magic_square

class TestMagicSquare(unittest.TestCase):
    def test_generate_magic_square(self):
        self.assertEqual(magic_square.generate_magic_square(3), [[8, 1, 6], [3, 5, 7], [4, 9, 2]])
        self.assertEqual(magic_square.generate_magic_square(5), [[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
        self.assertEqual(magic_square.generate_magic_square(7), [[30, 39, 48, 1, 10, 19, 28], [38, 47, 7, 9, 18, 27, 29], [46, 6, 8, 17, 26, 35, 37], [5, 14, 16, 25, 34, 36, 45], [13, 15, 24, 33, 42, 44, 4], [21, 23, 32, 41, 43, 3, 12], [22, 31, 40, 49, 2, 11, 20]])

if __name__ == "__main__":
    unittest.main()
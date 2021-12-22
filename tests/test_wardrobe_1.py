import unittest
from src.wardrobe_1 import wardrobe1


class TestWardrobe1(unittest.TestCase):
    # Remarks: Good start
    def test_wardrobe_size_0_return_an_empty(self):
        sizes, total = [1, 2, 3], 0
        self.assertListEqual([], wardrobe1(sizes, total))

    # Remarks: Bad -> (1) Jump; (2) Only 1 assert statement
    def test_wardrobe_return_all_combinations(self):
        sizes, total = [2, 4, 6, 8], 8
        self.assertListEqual(
            [[2, 2, 2, 2], [2, 2, 4], [2, 6], [4, 4], [8]],
            wardrobe1(sizes, total))

        sizes, total = [50, 75, 100, 129], 250
        self.assertListEqual(
            [[50, 50, 50, 50, 50], [50, 50, 50, 100], [
                50, 50, 75, 75], [50, 100, 100], [75, 75, 100]],
            wardrobe1(sizes, total))

import unittest
from src.wardrobe_2 import compute_shelf_combinations


class TestWardrobe2(unittest.TestCase):
    def test_compute_shelf_combinations_with_width_of_0_returns_an_empty_list(self):
        shelf_combinations = compute_shelf_combinations(0, [100])
        self.assertEqual([], shelf_combinations)

    def test_compute_shelf_combinations_with_1_shelf_that_fit_exactly(self):
        shelf_combinations = compute_shelf_combinations(1, [1])
        self.assertEqual([[1]], shelf_combinations)

    def test_compute_shelf_combinations_with_shelves_that_fit_exactly(self):
        shelf_combinations = compute_shelf_combinations(3, [1, 2])
        self.assertEqual([[1, 1, 1], [1, 2]], shelf_combinations)

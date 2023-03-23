import unittest
from main import get_index, move_pointees, play_game
import random

class MyTestCase(unittest.TestCase):

    def test_get_index(self):
        assert get_index(0, 0) == 0
        assert get_index(1, 1) == 16
        assert get_index(2, 3) == 33

    def move_pointees(coupon_values):
        new_coupon_values = coupon_values.copy()
        for i in range(num_coupons):
            row, col = divmod(i, board_size)
            if row == 0 or row == board_size - 1 or col == 0 or col == board_size - 1:
                # pointees on edge squares don't move
                continue
            else:
                # move Pointees to an adjacent square
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                direction = random.choice(directions)
                new_row, new_col = row + direction[0], col + direction[1]
                new_index = get_index(new_row, new_col)
                new_coupon_values[new_index] += 1
        return new_coupon_values

    def test_play_game(self):
        # creating a fixed seed for random number
        random.seed(42)

        # testing the game for 100 rounds
        play_game(100)


if __name__ == '__main__':
    unittest.main()

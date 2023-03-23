import random

BOARD_SIZE = 15
num_coupons = BOARD_SIZE ** 2

# initialize the number of Pointees
coupon_values = [1] * num_coupons


# define a function to calculate the index of a square given its row and column
def get_index(row, col):
    return row * BOARD_SIZE + col


# randomly move the pointees to adjacent squares
def move_pointees():
    for i in range(num_coupons):
        row, col = divmod(i, BOARD_SIZE)
        if row == 0 or row == BOARD_SIZE - 1 or col == 0 or col == BOARD_SIZE - 1:
            # pointees on edge squares don't move
            continue
        else:
            # randomly move pointees to an adjacent square
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            direction = random.choice(directions)
            new_row, new_col = row + direction[0], col + direction[1]
            new_index = get_index(new_row, new_col)
            coupon_values[new_index] += 1


# game for a specified number of rounds
def play_game(num_rounds):
    for i in range(num_rounds):
        move_pointees()
        if i == 24 or i == 49 or i == 99:

            # Redeem coupons for points after 25th, 50th, and 100th rounds
            points_per_coupon = []
            for j in range(num_coupons):
                if coupon_values[j] > 1:
                    points = coupon_values[j]
                    coupon_values[j] = 1
                    points_per_coupon.append((j, points))
            points_per_coupon.sort(key=lambda x: x[1], reverse=True)
            max_points = points_per_coupon[0][1]
            top_coupons = [x[0] for x in points_per_coupon if x[1] == max_points]
            print("Points per coupon at round", i + 1, ":", points_per_coupon)
            print("Coupon(s) with the highest number of points:", top_coupons, "with", max_points, "points")


play_game(100)

def compute_shelf_combinations(wardrobe_width, shelves_sizes):
    results = []
    if wardrobe_width == 0:
        return []

    for i in shelves_sizes:  # [1, 2]
        # wardrobe_width = 3
        # i = 2
        # 3 % 2 = 1

        remainder = wardrobe_width % i
        shelves_of_size_i_fits_exactly = remainder == 0
        shelves_of_size_i_fits_but_leaves_gap = wardrobe_width % i != i

        if shelves_of_size_i_fits_exactly:
            valid_combination = [i] * int(wardrobe_width / i)
            results.append(valid_combination)

        elif shelves_of_size_i_fits_but_leaves_gap:
            possible_combination = [i]  # [2]

            if remainder in shelves_sizes:
                # [2, 1]
                possible_combination.append(remainder)

            results.append(sorted(possible_combination))

    return results

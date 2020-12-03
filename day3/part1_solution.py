# Count Trees along a -1/3 slope

import math
import numpy as np


def calc_min_grid_width(txt, slope_x, slope_y):
    with open(txt) as f:
        lines = f.read().splitlines()
    height = len(lines)
    return math.ceil((height / slope_y) * slope_x)


def input_to_np(txt, width):
    with open(txt) as f:
        lines = f.read().splitlines()
    height = len(lines)
    while width % len(lines[0]) != 0:
        width += 1
    ski_map = np.zeros((height, width))
    for row_counter, row in enumerate(lines):
        column_counter = 0
        while column_counter < width:
            ski_map[row_counter, column_counter : column_counter + len(row)] = [
                0 if i == "." else 1 for i in row
            ]
            column_counter += len(row)
    return ski_map


def count_trees_on_path(ski_map, slope_x, slope_y):
    x_ptr = 0
    y_ptr = 0
    tree_count = 0
    while y_ptr < ski_map.shape[0]:
        if ski_map[y_ptr, x_ptr] == 1:
            tree_count += 1
        x_ptr += slope_x
        y_ptr += slope_y
    return tree_count


if __name__ == "__main__":
    slope_x = 3
    slope_y = 1
    width = calc_min_grid_width("input.txt", slope_x, slope_y)
    ski_map = input_to_np("input.txt", width)
    print(count_trees_on_path(ski_map, slope_x, slope_y))

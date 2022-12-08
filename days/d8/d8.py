import numpy as np


def pt1_checks(x):  # if invisible leave as 1, else set to 0
    out_array = np.ones_like(x)
    out_array[0] = 0
    out_array[-1] = 0
    for i in range(1, len(out_array) - 1):
        val_at_i = x[i]
        max_left = max(x[:i])
        max_right = max(x[i + 1:])
        if val_at_i > max_left or val_at_i > max_right:
            out_array[i] = 0
    return out_array


def pt1():
    row_wise = np.apply_along_axis(pt1_checks, axis=1, arr=data)
    column_wise = np.apply_along_axis(pt1_checks, axis=0, arr=data)
    combined = np.bitwise_and(row_wise.astype(int), column_wise.astype(int))
    return data.size - np.sum(combined)


def pt2_checks(x):  # numbers are visibility distance multiplied for that axis
    out_array = np.zeros_like(x)
    for i in range(1, len(out_array) - 1):
        val_at_i = x[i]
        left_viewing_distance = 0
        for y in np.flip(x[:i]):
            left_viewing_distance += 1
            if y >= val_at_i:
                break
        right_viewing_distance = 0
        for y in x[i + 1:]:
            right_viewing_distance += 1
            if y >= val_at_i:
                break
        out_array[i] = left_viewing_distance * right_viewing_distance
    return out_array


def pt2():
    row_wise = np.apply_along_axis(pt2_checks, axis=1, arr=data)
    column_wise = np.apply_along_axis(pt2_checks, axis=0, arr=data)
    combined = np.multiply(row_wise.astype(int), column_wise.astype(int))
    return np.amax(combined)


if __name__ == "__main__":
    data = np.genfromtxt("input.txt", delimiter=1)
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))

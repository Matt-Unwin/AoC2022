def pt1():
    for i in range(3, len(line)):
        test_set = {line[i], line[i - 1], line[i - 2], line[i - 3]}
        if len(test_set) == 4:
            return i + 1


def pt2():
    for i in range(12, len(line)):
        test_set = set()
        for x in range(0, 14):
            test_set.add(line[i-x])
        if len(test_set) == 14:
            return i + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))

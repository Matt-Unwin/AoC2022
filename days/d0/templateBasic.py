def pt1():
    for x in lines:
        print(x, sep="", end="")
    # code here


def pt2():
    for x in lines:
        print(x, sep="", end="")
    # code here


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))

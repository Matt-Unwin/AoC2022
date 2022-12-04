import re


def pt1():
    # (1a <= 2a & 1b >= 2b) OR (2a <= 1a & 2b >= 1b)
    # format : 1a-1b,2a-2b 0-1,2-3
    total = 0
    for line in lines:
        sp = re.split("[,-]", line)
        sp = list(map(int, sp))  # convert list to int as otherwise I think it compares by alphabetical order
        if (sp[0] <= sp[2] and sp[1] >= sp[3]) or (sp[2] <= sp[0] and sp[3] >= sp[1]):
            total += 1
    print(total)


def pt2():
    total = 0
    for line in lines:
        sp = re.split(",|-", line)
        sp = list(map(int, sp))
        if (sp[2] <= sp[0] <= sp[3]) or (sp[2] <= sp[1] <= sp[3]) or (sp[0] <= sp[2] <= sp[1]) or (sp[0] <= sp[3] <= sp[1]):
            total += 1
    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    pt1()
    pt2()

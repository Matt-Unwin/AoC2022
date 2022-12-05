import re
from collections import defaultdict


def create_data():
    #             [Q]     [G]     [M]
    #             [B] [S] [V]     [P] [R]
    #     [T]     [C] [F] [L]     [V] [N]
    # [Q] [P]     [H] [N] [S]     [W] [C]
    # [F] [G] [B] [J] [B] [N]     [Z] [L]
    # [L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
    # [S] [Z] [M] [G] [H] [C] [C] [H] [Z]
    # [R] [N] [S] [T] [P] [P] [W] [Q] [G]
    #  1   2   3   4   5   6   7   8   9
    # was meant to read from file in format above but was just quicker to type out
    return {
        1: ["R", "S", "L", "F", "Q"],
        2: ["N", "Z", "Q", "G", "P", "T"],
        3: ["S", "M", "Q", "B"],
        4: ["T", "G", "Z", "J", "H", "C", "B", "Q"],
        5: ["P", "H", "M", "B", "N", "F", "S"],
        6: ["P", "C", "Q", "N", "S", "L", "V", "G"],
        7: ["W", "C", "F"],
        8: ["Q", "H", "G", "Z", "W", "V", "P", "M"],
        9: ["G", "Z", "D", "L", "C", "N", "R"]
    }


def create_data_reading():
    # this produces an identical result to the above function but for some reason
    # gets changed to something different in the task functions
    in_str = """            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9"""

    dct = defaultdict(list)

    for line in in_str.splitlines():
        for i in range(9):
            index = i * 4 + 1
            found = re.findall("[A-Z]", line[index])
            if len(found) > 0:
                dct[i + 1].append(found[0])
    for lst in dct:
        dct[lst].reverse()
    return dct


def pt1():
    for line in lines:
        vals = re.findall("\d+", line)  # 0 = how many to move  1 = from   2= to
        for i in range(int(vals[0])):
            stacks[int(vals[2])].append(stacks[int(vals[1])].pop())
    for item in stacks:
        print(stacks[item].pop(), end="")


def pt2():
    for line in lines:
        vals = re.findall("\d+", line)  # 0 = how many to move  1 = from   2= to
        intermediate_list = []
        for i in range(int(vals[0])):
            intermediate_list.append(stacks[int(vals[1])].pop())
        intermediate_list.reverse()
        stacks[int(vals[2])].extend(intermediate_list)
    for item in stacks:
        print(stacks[item].pop(), end="")


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    stacks = create_data()
    pt1()
    print()
    stacks = create_data()
    pt2()

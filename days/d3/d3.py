from collections import defaultdict


def pt1():
    # split the line into two
    # find which character appears in both (dict)
    # convert to number
    # sum
    total = 0

    for line in lines:
        first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
        char_set = set()
        for character in first_half:
            char_set.add(character)
        in_both_char = ""
        for character in second_half:
            if character in char_set:
                in_both_char = character
                break

        if in_both_char.isupper():
            total += (ord(in_both_char)-38)
        else:
            total += (ord(in_both_char)-96)

    print(total)


def pt2():
    total = 0

    section_counter = 1
    dct = defaultdict(int)

    for line in lines:
        for character in set(line):
            dct[character] += 1

        if section_counter == 3:
            common_char = list(dct.keys())[list(dct.values()).index(3)]
            if common_char.isupper():
                total += (ord(common_char) - 38)
            else:
                total += (ord(common_char) - 96)

            section_counter = 0
            dct = defaultdict(int)
        section_counter += 1
    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    pt1()
    pt2()

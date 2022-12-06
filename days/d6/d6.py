def dif_seq_finder(seq_len):
    for i in range(seq_len-1, len(line)):
        test_set = set([x for x in line[i - (seq_len - 1): i+1]])
        if len(test_set) == seq_len:
            return i + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read()
    print("part1: " + str(dif_seq_finder(4)))
    print("part2: " + str(dif_seq_finder(14)))

def get_file_structure():
    top_dct = {}
    current_location = [top_dct]
    for line in lines:
        spl = line.split(" ")
        if spl[0] == "$":  # is command
            if spl[1] == "cd":  # change directory - can ignore ls
                if spl[2] == "..":
                    current_location.pop()
                else:
                    dct = current_location[-1]
                    dct[spl[2]] = {}
                    dct = dct[spl[2]]
                    current_location.append(dct)
        else:  # is result
            if spl[0] != "dir":  # we don't care about dir, unless cd.
                current_location[-1][spl[1]] = int(spl[0])
    return top_dct


def recursive_summer(dct):
    total = 0
    for key in dct:
        if type(dct[key]) == dict:
            total += recursive_summer(dct[key])
        else:
            total += dct[key]
    dct["__SUM__"] = total
    return total


def recursive_max_val(dct, lst, val):
    for key in dct:
        if type(dct[key]) == dict:
            recursive_max_val(dct[key], lst, val)
    if dct["__SUM__"] <= val:
        lst.append(dct["__SUM__"])


def recursive_min_val(dct, lst, val):
    for key in dct:
        if type(dct[key]) == dict:
            recursive_min_val(dct[key], lst, val)
    if dct["__SUM__"] >= val:
        lst.append(dct["__SUM__"])


def pt1():
    lst = []
    recursive_max_val(file_structure, lst, 100000)
    return sum(lst)


def pt2():
    lst = []
    recursive_min_val(file_structure, lst, 2143088)
    return min(lst)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    file_structure = get_file_structure()
    recursive_summer(file_structure)
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))

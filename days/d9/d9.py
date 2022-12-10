import numpy as np

grid = np.zeros((999, 999))


def make_move(direction, distance, current_head, current_tail):
    #  never worry about bounds checking as if we reach them the array should be bigger
    distance = int(distance)
    # what movement the tail has to take to reach the head

    # this records the locations of the head on the grid which isn't necessary. Record tail only
    for i in range(0, distance):
        relative_position = tuple(np.subtract(current_head, current_tail))
        match direction:
            case "U":
                current_head = (current_head[0] - 1, current_head[1])
                if relative_position[0] == -1:
                    current_tail = (current_head[0] + 1, current_head[1])
            case "D":
                current_head = (current_head[0] + 1, current_head[1])
                if relative_position[0] == 1:
                    current_tail = (current_head[0] - 1, current_head[1])
            case "L":
                current_head = (current_head[0], current_head[1] - 1)
                if relative_position[1] == -1:
                    current_tail = (current_head[0], current_head[1] + 1)
            case "R":
                current_head = (current_head[0], current_head[1] + 1)
                if relative_position[1] == 1:
                    current_tail = (current_head[0], current_head[1] - 1)
        grid[current_tail[0]][current_tail[1]] = 1
    return current_head, current_tail


def pt1():
    grid[499][499] = 1  # 1 if visited, 0 if not
    current_head = (499, 499)
    current_tail = (499, 499)
    for command in commands:
        direction, distance = command.split(" ")
        current_head, current_tail = make_move(direction, distance, current_head, current_tail)
    return np.count_nonzero(grid)


def pt2():
    return


if __name__ == "__main__":
    with open("input.txt") as f:
        commands = f.read().splitlines()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))

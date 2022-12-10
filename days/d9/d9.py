import numpy as np


def make_move(direction, distance, current_head, current_tail, is_tail=False, record_grid=True):
    #  never worry about bounds checking as if we reach them the array should be bigger
    distance = int(distance)
    # what movement the tail has to take to reach the head

    # this records the locations of the head on the grid which isn't necessary. Record tail only
    for i in range(0, distance):
        relative_position = tuple(np.subtract(current_head, current_tail))
        match direction:
            case "U":
                if not is_tail:
                    current_head = (current_head[0] - 1, current_head[1])
                if relative_position[0] < 0:
                    current_tail = (current_head[0] + 1, current_head[1])
            case "D":
                if not is_tail:
                    current_head = (current_head[0] + 1, current_head[1])
                if relative_position[0] > 0:
                    current_tail = (current_head[0] - 1, current_head[1])
            case "L":
                if not is_tail:
                    current_head = (current_head[0], current_head[1] - 1)
                if relative_position[1] < 0:
                    current_tail = (current_head[0], current_head[1] + 1)
            case "R":
                if not is_tail:
                    current_head = (current_head[0], current_head[1] + 1)
                if relative_position[1] > 0:
                    current_tail = (current_head[0], current_head[1] - 1)
        if record_grid:
            grid[current_tail[0]][current_tail[1]] = 1
    return current_head, current_tail


def pt1():
    grid[1000][1000] = 1  # 1 if visited, 0 if not
    current_head = (1000, 1000)
    current_tail = (1000, 1000)
    for command in commands:
        direction, distance = command.split(" ")
        current_head, current_tail = make_move(direction, distance, current_head, current_tail)
    return np.count_nonzero(grid)


def pt2():
    grid[1000][1000] = 1  # 1 if visited, 0 if not
    snake_list = [(1000, 1000)] * 10
    for command in commands:
        direction, distance = command.split(" ")
        for i in range(1, len(snake_list)):
            record_grid = False
            is_tail = True
            if i == len(snake_list) - 1:
                record_grid = True
            if i == 1:
                is_tail = False
            snake_list[i - 1], snake_list[i] = make_move(direction, distance, snake_list[i - 1], snake_list[i], is_tail, record_grid)
    return np.count_nonzero(grid)


if __name__ == "__main__":
    with open("input.txt") as f:
        commands = f.read().splitlines()
    grid = np.zeros((2000, 2000))
    print("part1: " + str(pt1()))
    grid = np.zeros((2000, 2000))
    print("part2: " + str(pt2()))

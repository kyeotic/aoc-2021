import os
from functools import reduce

file_path = '../inputs/day-09.txt'


def part1():
    grid = get_input()

    return sum([grid[y][x] + 1 for x, y in get_low_points(grid)])


def part2():
    grid = get_input()

    return reduce(lambda sum, n: sum * n, [x for x in sorted([len(basin) for basin in get_basins(grid)], reverse=True)[:3]])


def get_low_points(grid):
    return [(x, y) for y, line in enumerate(grid) for x, h in enumerate(line) if all(h < get_point(grid, n) for n in get_adjacent(grid, x, y))]


def get_basins(grid):
    basins = []
    low_points = get_low_points(grid)

    for start in low_points:
        basin = []
        to_search = [start]
        closed = set(to_search)

        closed.add(start)

        while len(to_search) > 0:
            point = to_search.pop()
            basin.append(point)
            neighbors = get_adjacent(grid, point[0], point[1])
            to_search = to_search + \
                [p for p in neighbors if p not in closed
                 and get_point(grid, p) is not 9]
            closed.update(neighbors)

        basins.append(basin)

    return basins


def get_point(grid, point):
    return grid[point[1]][point[0]]


def get_adjacent(grid, x, y):
    results = []

    # left
    if x > 0:
        results.append((x - 1, y))

    # right
    if x < len(grid[0]) - 1:
        results.append((x + 1, y))

    # up
    if y > 0:
        results.append((x, y - 1))

    # down:
    if y < len(grid) - 1:
        results.append((x, y + 1))

    # print(x, y, results)

    return results


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read().splitlines()

    return [[int(x) for x in line] for line in input]


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

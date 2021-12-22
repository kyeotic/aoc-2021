import os
from functools import reduce

file_path = '../inputs/day-05.txt'


def part1():
    segments = get_input()

    straight_lines = [s for s in segments if s[0]
                      [0] == s[1][0] or s[0][1] == s[1][1]]
    grid = map_lines(straight_lines)

    # print_grid(grid)
    return len([cell for row in grid.values() for cell in row.values() if cell >= 2])


def part2():
    segments = get_input()

    grid = map_lines(segments)

    # print_grid(grid)
    return len([cell for row in grid.values() for cell in row.values() if cell >= 2])


def map_lines(segments):
    grid = {}

    for start, end in segments:
        cursor = start
        while cursor[0] != end[0] or cursor[1] != end[1]:
            # print(f'mark {cursor}')
            mark(grid, cursor)
            cursor = move_toward(cursor, end)
        mark(grid, end)
    return grid


def mark(grid, point):
    x, y = point
    if not x in grid:
        grid[x] = {}
    row = grid[x]
    row[y] = 1 if not y in row else row[y] + 1


def move_toward(current, target):
    xC, yC = current
    xT, yT = target

    # already matched
    if (xC == xT and yC == yT):
        return target

    return (step_toward(xC, xT), step_toward(yC, yT))


def step_toward(n, t):
    return n + 1 if n < t else n - 1 if n > t else n


def print_grid(grid):
    # print(grid)
    for k, row in grid.items():
        print(k, row)


def get_input():

    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read().splitlines()

    # ( (x1, y1), (x2, y2) )
    segments = []
    for segment in input:
        segments.append(tuple(
            (int(points[0]), int(points[1])) for points in ([point.split(',') for point in segment.split(' -> ')])
        ))

    return segments


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

import os

file_path = '../inputs/day-11.txt'
adjacent = [
    (-1, -1),  # top-left
    (0, -1),  # top
    (1, -1),  # top-right
    (1, 0),   # right
    (1, 1),   # bottom-right
    (0, 1),   # bottom
    (-1, 1),   # bottom-left
    (-1, 0),  # left
]


def part1():
    grid = get_input()

    return sum(len(tick(grid)) for _ in range(0, 100))


def part2():
    grid = get_input()

    target = len(grid) * len(grid[0])
    i = 0
    while True:
        i += 1
        flashers = tick(grid)
        if len(flashers) >= target:
            break

    return i


def tick(grid):
    # first increment all by one

    # store flash points twice: one for all flashers, and one for flashers-to-cascade
    # search for nines, add to flash points and cascade
    # while cascade
    # pop cascade
    # get neighbors that are not in flashers
    # increment and add to flashers and cascade

    # reset flashers, return coordinates

    flashers = set()
    cascade = set()

    def increment(x, y):
        point = (x, y)
        octopus = grid[y][x]
        octopus += 1
        grid[y][x] = octopus
        if octopus > 9:
            flashers.add(point)
            cascade.add(point)

    # step 1, increment all
    for y, line in enumerate(grid):
        for x, _ in enumerate(line):
            increment(x, y)

    # step 2, cascade
    while len(cascade) > 0:
        flasher = cascade.pop()
        to_flash = [point for point in get_neighbors(grid, flasher)
                    if point not in flashers]

        for x, y in to_flash:
            increment(x, y)

    # step 3, reset
    for x, y in flashers:
        grid[y][x] = 0

    return flashers


def get_neighbors(grid, point):
    return [(x, y) for x, y in [(point[0] + aX, point[1] + aY) for aX, aY in adjacent]
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid)]


def print_grid(grid):
    for row in grid:
        print(row)
    print('')


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read().splitlines()

    return [[int(x) for x in line] for line in input]


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

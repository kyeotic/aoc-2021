import os
from functools import reduce

file_path = '../inputs/day-N.txt'


def part1():
    input = get_input()

    return 0


def part2():
    input = get_input()

    return 0


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read()
    return input.splitlines()


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

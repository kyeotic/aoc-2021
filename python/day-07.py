import os
from statistics import median

file_path = '../inputs/day-07.txt'


def part1():
    return find_lowest_transfer(get_input(), linear_transfer_cost)


def part2():
    return find_lowest_transfer(get_input(), accelerating_transfer_cost)


def find_lowest_transfer(positions, cost_fn):
    return min([cost_fn(positions, x) for x in range(0, max(positions))])


def linear_transfer_cost(positions, target):
    return sum([abs(x - target) for x in positions])


def accelerating_transfer_cost(positions, target):
    return sum([sequence_cost(x, target) for x in positions])


def sequence_cost(current, target):
    return int(abs(current - target) * (abs(current - target) + 1) / 2)


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read()
    return [int(x) for x in input.split(',')]


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

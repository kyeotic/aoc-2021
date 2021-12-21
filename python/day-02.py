import os
from functools import reduce


def part1():
    input = get_input()
    position = {
        "x": 0,
        "y": 0
    }

    reduce(lambda pos, step: update_position(
        pos, step), list(map(parse_step, input)), position)

    return position['x'] * position['y']


def part2():
    input = get_input()
    position = {
        "x": 0,
        "y": 0,
        "aim": 0
    }

    reduce(lambda pos, step: update_aim(
        pos, step), list(map(parse_step, input)), position)

    return position['x'] * position['y']


def parse_step(line):
    dir, amount = line.split(' ')
    return (dir, int(amount))


def update_position(position, step):
    dir, amount = step

    match dir:
        case 'forward':
            position['x'] += amount
        case 'up':
            position['y'] -= amount
        case 'down':
            position['y'] += amount

    return position


def update_aim(position, step):
    dir, amount = step

    match dir:
        case 'forward':
            position['x'] += amount
            position['y'] += position['aim'] * amount
        case 'up':
            position['aim'] -= amount
        case 'down':
            position['aim'] += amount

    return position


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              '../inputs/day-02.txt'), 'r').read()
    return input.splitlines()


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

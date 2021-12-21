import os


def part1():
    input = get_input()
    return [(b > a) for a, b in zip(input, input[1:])].count(True)


def part2():
    input = get_input()
    return [(b > a) for a, b in zip(input, input[3:])].count(True)


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              '../inputs/day-01.txt'), 'r').read()
    return list(map(int, input.splitlines()))


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 1: ' + str(part2()))

import os
from functools import reduce

file_path = '../inputs/day-06.txt'


def part1():
    fish = get_input()

    print(fish)

    return simulate(fish, 80)


def part2():
    fish = get_input()

    return simulate(fish, 256)


def simulate(fish, days):

    while days > 0:
        fish = tick(fish, 6, 8)
        days -= 1
    return sum(fish.values())


def tick(items, cycle, delay):
    new_items = 0
    tomorrow = {}

    for days, count in items.items():
        if days == 0:
            new_items = count
        else:
            tomorrow[days - 1] = count

    if new_items > 0:
        inc(tomorrow, cycle, new_items)
        inc(tomorrow, delay, new_items)

    return tomorrow


def inc(dic, key, val):
    if key not in dic:
        dic[key] = val
    else:
        dic[key] += val


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read()

    fish = {}
    for val in input.split(','):
        inc(fish, int(val), 1)

    return fish


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

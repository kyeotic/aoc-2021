import os
from functools import reduce

file_path = '../inputs/day-03.txt'


def part1():
    input = get_input()

    reports = [int(x, 2) for x in input]
    bit_len = len(input[0])

    summary = {}
    for n in range(bit_len):
        summary[n] = 0

    summarize(summary, reports)
    gamma = get_gamma(summary, len(input))
    epsilon = flip_bits(gamma, bit_len)

    return gamma * epsilon


def part2():
    input = get_input()

    oxygen_rating = get_rating(input, select_oxygen)
    co2_rating = get_rating(input, select_co2)

    return int(oxygen_rating, 2) * int(co2_rating, 2)


def summarize(summary, reports):
    num_bits = len(summary)

    for report in reports:
        for pos, bit in enumerate([(report >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]):
            summary[pos] += bit

    return summary


def get_gamma(summary, length):
    result = ''
    for key in sorted(summary):
        result += '1' if summary[key] > length / 2 else '0'
    return int(result, 2)


def get_rating(num_input, predicate):
    nums = num_input[:]
    limit = len(num_input[0])

    cursor = 0
    while len(nums) > 1 and cursor < limit:
        ratio = len([x[cursor]for x in nums if x[cursor] == '1']) \
            / len(nums)
        nums = [val for val in nums if predicate(val[cursor], ratio)]
        cursor += 1

    if len(nums) > 1:
        raise ValueError(
            f'Rating was unable to filter to a single number, cursor: {cursor}/{limit} remianing: {nums}')

    return nums[0]


def select_oxygen(value, avg):
    return value == ('1' if avg >= 0.5 else '0')


def select_co2(value, avg):
    return value == ('0' if avg >= 0.5 else '1')


def flip_bits(num, bits):
    mask = (1 << bits) - 1
    return ~num & mask


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read()
    return input.splitlines()


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

import os
from collections import deque
from enum import Enum

file_path = '../inputs/day-10.txt'
illegal_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
closers = pairs.values()
openers = pairs.keys()


class LineTypes(Enum):
    Normal = "normal"
    Incomplete = "incomplete"
    Invalid = "invalid"


def part1():
    lines = get_input()

    return sum(illegal_scores[error] for line_type, error in [parse_line(line) for line in lines] if line_type is LineTypes.Invalid)


def part2():
    lines = get_input()

    scores = [score_line(stack) for line_type, stack in [parse_line(
        line) for line in lines] if line_type is LineTypes.Incomplete]

    return sorted(scores)[len(scores)//2]


def parse_line(line):
    symbols = deque(list(line))
    stack = []
    while len(symbols) > 0:
        cursor = symbols.popleft()
        if cursor in openers:
            stack.append(cursor)
            continue
        elif cursor in closers:
            if cursor is pairs[stack[-1]]:
                stack.pop()
                continue
            else:
                return LineTypes.Invalid, cursor
        else:
            raise ValueError(f'Unknown symbol {cursor}')

    if len(stack) > 0:
        return LineTypes.Incomplete, [pairs[s] for s in stack]

    return LineTypes.Normal, None


def score_line(stack):
    score = 0
    stack = deque(reversed(stack))
    while len(stack) > 0:
        cursor = stack.popleft()
        score = score * 5 + completion_scores[cursor]
    return score


def get_input():
    return open(os.path.join(os.path.dirname(__file__),
                             file_path), 'r').read().splitlines()


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

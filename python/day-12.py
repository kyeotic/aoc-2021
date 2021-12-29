import os
from collections import defaultdict, Counter
import colored_traceback.auto

file_path = '../inputs/day-12.txt'

# Node Constants
START = 'start'
END = 'end'


def part1():
    edges = get_input()

    def can_visit(path, node):
        if node.isupper():
            return True
        return node not in path

    return len(get_unique_paths(edges, can_visit=can_visit))


def part2():
    edges = get_input()

    def can_visit(path, node):
        if node.isupper() or node not in path:
            return True
        return max(n for n in Counter([c for c in path if c.islower()]).values()) < 2

    return len(get_unique_paths(edges, can_visit=can_visit))


def get_unique_paths(edges, can_visit, start=START, end=END):
    solutions = []
    path = []

    def add_path(path):
        solutions.append(path[:])

    traverse(edges, start, end, path, add_path, can_visit)

    return solutions


def traverse(edges, current, end, path, save_path, can_visit):
    path.append(current)

    if (current == end):
        save_path(path)
    else:
        for neighbor in [n for n in edges[current] if can_visit(path, n)]:
            traverse(edges, neighbor, end, path, save_path, can_visit)

    path.pop()


def get_input():
    input = open(os.path.join(os.path.dirname(__file__),
                              file_path), 'r').read().splitlines()
    edges = [tuple(line.split('-')) for line in input]
    graph = defaultdict(list)
    for start, end in edges:
        if end != START:
            graph[start].append(end)
        if start != START and end != END:
            graph[end].append(start)

    return graph


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

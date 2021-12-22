import os
from collections import deque

file_path = '../inputs/day-04.txt'


def part1():
    draws, boards = get_input()

    while True:
        draw = draws.popleft()
        winners = mark_boards(boards, draw)
        if len(winners):
            winner = winners[0]
            break
        if len(draws) == 0:
            raise ValueError("No draws left, no winner found")

    return sum([int(cell[0])
                for row in winner for cell in row if cell[1] is False]) * int(draw)


def part2():
    draws, boards = get_input()

    winners = []
    while len(boards):
        draw = draws.popleft()
        round_winners = mark_boards(boards, draw)
        if len(round_winners) > 0:
            for winner in round_winners:
                boards.remove(winner)
                winners.append((winner, draw))
        if len(draws) == 0:
            break

    final_winner = winners[-1][0]
    final_draw = winners[-1][1]

    return sum([int(cell[0])
                for row in final_winner for cell in row if cell[1] is False]) * int(final_draw)


# def parse

def mark_boards(boards, draw):
    winners = []
    for board in boards:
        x, y = find_cell(board, draw)

        if x is None:
            continue

        # mark the cell
        board[x][y][1] = True

        if all(mark for [_, mark] in get_row(board, x)) or all(mark for [_, mark] in get_column(board, y)):
            winners.append(board)
    return winners


def find_cell(board, val):
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell[0] == val:
                return x, y
    return None, None


def get_row(board, x):
    return board[x]


def get_column(board, y):
    return [row[y] for row in board]


def get_input():
    input = deque(open(os.path.join(os.path.dirname(__file__),
                                    file_path), 'r').read().splitlines())

    draws = deque(input.popleft().split(','))
    boards = []

    board = []
    while len(input) > 0:
        line = input.popleft()

        if not line:
            if len(board) > 0:
                boards.append(board)
            board = []
            continue

        board.append([[cell, False] for cell in line.split()])

    if len(board) > 0:
        boards.append(board)

    # for board in boards:
    #     print(board)

    return draws, boards


def print_board(board):
    for row in board:
        print(row)


if __name__ == "__main__":
    print('Part 1: ' + str(part1()))
    print('Part 2: ' + str(part2()))

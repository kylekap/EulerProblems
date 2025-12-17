import logging
import time
from itertools import combinations, combinations_with_replacement, permutations, product  # noqa: F401
from pathlib import Path  # noqa: F401

import solved  # noqa: F401
import util  # noqa: F401

logger = logging.getLogger(__name__)  # put this in each file


def countifs(iterable, condition):
    return sum(1 for x in iterable if condition(x))


def countall(iterable):
    di = {}
    for x in iterable:
        di[x] = di.get(x, 0) + 1
    return di


class Sudoku:
    def __init__(self, board):
        self.board = board
        self.guess_board = [[[] for _ in range(9)] for _ in range(9)]
        self.set_possibilities()

    def __str__(self):
        self.print_board(board=self.board)
        return ""

    def print_board(self, **kwargs):
        for row in kwargs.get("board", self.board):  # self.board:
            print(row)

    def get_row(self, x):
        return self.board[x]

    def get_col(self, y):
        return [self.board[i][y] for i in range(9)]

    def get_area(self, x, y):
        return [self.board[3 * (x // 3) + i][3 * (y // 3) + j] for i, j in product(range(3), range(3))]

    def set_possibilities(self):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    self.guess_board[x][y] = [i for i in range(1, 10) if not self.check_all(x, y, i)] # Get the possible answers
                else:
                    self.guess_board[x][y] = [] # If the box is already filled, there's no other possible answers

    def exact_solve(self):
        while 1 in countall([len(self.guess_board[x][y if isinstance(self.guess_board[x][y], list) else 0]) for x in range(9) for y in range(9)]): # Get the number of possible answers for each empty box. If any are 1, solve that one
            for x in range(9):
                for y in range(9):
                    if len(self.guess_board[x][y]) == 1: # If there's only one possible answer
                        self.board[x][y] = self.guess_board[x][y][0] # Set the box to that answer
                        self.set_possibilities() # Update the possibilities
        return self.board


    def guess_and_check(self):
        return None


    def check_row(self, x, num):
        return num in self.get_row(x)

    def check_col(self, y, num):
        return num in self.get_col(y)

    def check_box(self, x, y, num):
        return num in self.get_area(x, y)

    def check_all(self, x, y, num):
        return self.check_row(x, num) or self.check_col(y, num) or self.check_box(x, y, num)


test_board = [[0,0,3,0,2,0,6,0,0],
              [9,0,0,3,0,5,0,0,1],
              [0,0,1,8,0,6,4,0,0],
              [0,0,8,1,0,2,9,0,0],
              [7,0,0,0,0,0,0,0,8],
              [0,0,6,7,0,8,2,0,0],
              [0,0,2,6,0,9,5,0,0],
              [8,0,0,2,0,3,0,0,9],
              [0,0,5,0,1,0,3,0,0]]

test_board2= [[2,0,0,0,8,0,3,0,0],
              [0,6,0,0,7,0,0,8,4],
              [0,3,0,5,0,0,2,0,9],
              [0,0,0,1,0,5,4,0,8],
              [0,0,0,0,0,0,0,0,0],
              [4,0,2,7,0,6,0,0,0],
              [3,0,1,0,0,7,0,4,0],
              [7,2,0,0,4,0,0,6,0],
              [0,0,4,0,1,0,0,0,3]]

test_test_board = [["00", "01", "02", "03", "04", "05", "06", "07", "08"],
                   ["10", "11", "12", "13", "14", "15", "16", "17", "18"],
                   ["20", "21", "22", "23", "24", "25", "26", "27", "28"],
                   ["30", "31", "32", "33", "34", "35", "36", "37", "38"],
                   ["40", "41", "42", "43", "44", "45", "46", "47", "48"],
                   ["50", "51", "52", "53", "54", "55", "56", "57", "58"],
                   ["60", "61", "62", "63", "64", "65", "66", "67", "68"],
                   ["70", "71", "72", "73", "74", "75", "76", "77", "78"],
                   ["80", "81", "82", "83", "84", "85", "86", "87", "88"]]


def generate_number_from_digits(*args):
    return int("".join([str(i) for i in args]))


def active_problem():
    # Active problem
    r"""Commented out.

    data = util.import_text_file("data/0096_sudoku.txt")
    active_board = []
    first_three_spots_total = 0.

    for line in data:
        if line in {"\n", "\r\n"}:
            continue
        if line.startswith("Grid"):
            continue
        if line == "":
            continue
        if len(active_board) == 9:
            sudoku_to_solve = Sudoku(active_board)
            solved, iterations = sudoku_to_solve.solve()
            print(sudoku_to_solve, iterations)
            first_three_spots_total += generate_number_from_digits(sudoku_to_solve.board[0][0], sudoku_to_solve.board[0][1], sudoku_to_solve.board[0][2])
            active_board = []
            continue

        cleaned_line = line.replace("  ", " ").replace(" ", "").replace("\n", "").replace("\r\n", "")
        cleaned_line = [int(i) for i in cleaned_line]
        active_board.append(cleaned_line)

    return first_three_spots_total
    """
    sudoku_to_solve = Sudoku(test_board2)
    sudoku_to_solve.print_board(board=sudoku_to_solve.guess_board)
    sudoku_to_solve.exact_solve()
    return sudoku_to_solve

def main():
    # Main function
    try:
        start_time = time.time()
        answer = active_problem()
        sec = time.time() - start_time
        print(f"Answer: {answer} in {sec} seconds ---")
    except Exception as E:
        logger.warning(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)
        raise


if __name__ == "__main__":
    """[summary]"""
    main()
    """Run main function if this is the main module."""

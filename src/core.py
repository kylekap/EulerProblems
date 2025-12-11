import logging
import random  # noqa: F401
import time
from itertools import combinations, combinations_with_replacement, permutations, product  # noqa: F401
from pathlib import Path  # noqa: F401

import solved  # noqa: F401
import util  # noqa: F401

logger = logging.getLogger(__name__)  # put this in each file

board = [
    "GO", #00
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "JAIL", #10

    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP", #20

    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J", #30

    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2", #39
]

def top_x_from_dict(num_values, my_dict):
    return dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:num_values])

def print_dict(di):
    for k, v in di.items():
        print(f"{k}: {v}")

def active_problem(iterations=1_000_000):
    game = Monopoly(dice_size=4)
    for _ in range(iterations):
        game.turn()
    print(game.DEBUG_jailed_count)
    di = top_x_from_dict(3, game.visited_squares)
    print_dict(dict(sorted(game.visited_squares.items(), key=lambda x: x[1], reverse=True)))
    return "".join(f"{board.index(x):02d}" for x in di), di


class Monopoly:
    def __init__(self, dice_size=6, num_doubles_to_jail=3, num_community_chest=16, num_chance=16, seed=None):
        self.CC = self.shuffle(["GO", "JAIL"]+[""]*(num_community_chest-2))
        self.CH = self.shuffle(["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", -3]+[""]*(num_chance-10))
        self.dice_size = dice_size
        self.current_square = 0
        self.visited_squares = dict.fromkeys(board, 0)
        self.num_doubles_to_jail = num_doubles_to_jail
        self.doubles_to_jail_streak = 0
        self.DEBUG_jailed_count = 0

    def shuffle(self, li):
        return random.sample(li, len(li))

    def turn(self):
        # Roll dice
        # Check for doubles, move to jail if 3x
        # Move player
        # Do square effect
        # Do card effect
        # Log results

        card = ""
        dice_result, is_double = self.roll_n(2)

        if is_double:
            self.doubles_to_jail_streak += 1
            if self.doubles_to_jail_streak == self.num_doubles_to_jail:
                self.DEBUG_jailed_count += 1
                next_square = self.move_card("JAIL")
                self.doubles_to_jail_streak = 0
            else:
                next_square = self.move_dice(sum(dice_result))
        else:
            self.doubles_to_jail_streak = 0
            next_square = self.move_dice(sum(dice_result))

        if board[next_square].startswith("CC"):# Community Chest
            card, self.CC = self.draw_card(self.CC)
            if card != "":
                next_square = self.move_card(card)
        elif board[next_square].startswith("CH"): # Chance
            card, self.CH = self.draw_card(self.CH)
            if isinstance(card, int): # Check if card is a number
                next_square = self.move_dice(card)
            elif card != "": # Check if card is anything else
                next_square = self.move_card(card)
        if board[next_square] == "G2J": # Jail
            next_square = self.move_card("JAIL")

        self.current_square = next_square

        self.visited_squares[board[self.current_square]] += 1

    def roll(self):
        # Roll dice
        return random.randint(1, self.dice_size)  # noqa: S311

    def roll_n(self, n):
        # Returns a list of n rolls, and True if they are all the same
        rolls = [self.roll() for _ in range(n)]
        return rolls, len(set(rolls))==1

    def move_dice(self, dice_result):
        next_square = self.current_square + dice_result # Next square
        if next_square > len(board) - 1: # You can move forwards, so wrap
            next_square -= len(board)
        elif next_square < 0: # You can move backwards, so wrap
            next_square += len(board)
        return next_square

    def move_card(self, card):
        position = self.current_square
        while not board[position].startswith(card):
            position = (position + 1) % len(board)
        return position

    def draw_card(self, cards):
        li = cards.copy()
        drawn = li.pop(0)
        li.insert(len(li), drawn)
        return drawn, li



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

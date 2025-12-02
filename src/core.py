import logging
import time
from itertools import combinations, combinations_with_replacement, permutations, product  # noqa: F401
from pathlib import Path  # noqa: F401

import solved  # noqa: F401
import util  # noqa: F401

logger = logging.getLogger(__name__)  # put this in each file


def active_problem(limit=100):
    e = [2]
    i = 1
    while len(e) < limit:
        e += [1, i*2, 1]
        i += 1
    e = e[0:limit]
    e.reverse()
    numerator, denominator = 1, e[0]

    for x in range(1,limit):
        numerator, denominator = denominator, e[x]*denominator + numerator

    return util.sum_digits_powers(denominator,1)


def active_problem2():
    return solved.problem92_alt()


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

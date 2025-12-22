import logging
import time
from itertools import combinations, combinations_with_replacement, permutations, product  # noqa: F401
from pathlib import Path  # noqa: F401

import solved  # noqa: F401
import util  # noqa: F401

logger = logging.getLogger(__name__)  # put this in each file


def active_problem():
    # Terrible answer to #91. Way too slow - need to find a better way
    def find_chain(x, max_limit=1_000_000):
        loop_val = x
        chain = [x]
        while True:
            fd = util.add_list(list(set(util.find_all_divisors(loop_val))))
            if fd == chain[0]:
                break
            if fd in chain:
                chain = []
                break
            if max_limit and fd > max_limit:
                chain = []
                break
            chain.append(fd)
            loop_val = fd
        return chain

    max_len = 0
    max_chain = []
    for x in range(1, 1_000_000):
        chain = find_chain(x)
        if len(chain) > max_len:
            max_len = len(chain)
            max_chain = chain
    return min(max_chain), max_chain


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

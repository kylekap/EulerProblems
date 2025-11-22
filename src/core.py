import logging
import time
from itertools import combinations, combinations_with_replacement, permutations, product  # noqa: F401
from pathlib import Path  # noqa: F401

import solved  # noqa: F401
import util  # noqa: F401

logger = logging.getLogger(__name__)  # put this in each file


def active_problem():
    ok_set = {89}
    not_ok_set = {1}
    running_list = []
    for i in range(1, 100000):
        curr = i
        running_list = [i]
        while curr not in ok_set and curr not in not_ok_set:
            curr = sum([ea**2 for ea in util.convert_int_to_list(curr)])
            running_list.append(curr)
        if curr in ok_set:
            ok_set = ok_set.union(set(running_list))
        else:
            not_ok_set = not_ok_set.union(set(running_list))
    return len(ok_set)


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

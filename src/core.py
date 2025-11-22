import time
from itertools import combinations, combinations_with_replacement, permutations, product  # noqa: F401
from pathlib import Path  # noqa: F401

import solved  # noqa: F401
import util  # noqa: F401


def active_problem():
    return None


def main():
    # Main function
    try:
        start_time = time.time()
        answer = active_problem()
        sec = time.time() - start_time
        print(f"Answer: {answer} in {sec} seconds ---")
    except Exception as e:  # noqa: BLE001
        print(e)


if __name__ == "__main__":
    """[summary]"""
    main()
    """Run main function if this is the main module."""

import logging

import util

logging.basicConfig(
    filename="reports/all.log",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
)  # put this only in main core.py file

logger = logging.getLogger(__name__)  # put this in each file


def active_problem(digits, idx):
    from itertools import permutations

    perms = list(permutations(digits))
    perms.sort()
    return perms[idx]


def main():
    # Main function
    try:
        print(active_problem(digits=[0,1,2,3,4,5,6,7,8,9], idx = 999999))
    except Exception as E:
        logger.warning(type(E).__name__, __file__, E.__traceback__.tb_lineno, "\n", E)
        raise


if __name__ == "__main__":
    """[summary]"""
    main()


import csv
from pathlib import Path


def is_prime(n):
    """Return True if n is prime. False otherwise.

    Args:
        n (int): number to check

    Returns:
        bool: True if n is prime. False otherwise.

    """
    if isinstance(n, str):
        n = int(n)
    if n in (2, 3):
        return True
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def prime_list(max_value):
    """Generate a list of prime numbers below max_value.

    Args:
        max_value (list): list of prime numbers

    Returns:
        list: list of prime numbers below n

    """
    prime = [True] * max_value
    for i in range(3, int(max_value**0.5) + 1, 2):
        if prime[i]:
            prime[i * i :: 2 * i] = [False] * ((max_value - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, max_value, 2) if prime[i]]


def is_palindrome(item):
    """Return True of provided item is a palindrome.

    Args:
        item (int, str): check if palindrome

    Returns:
        bool: True of provided item is a palindrome, False otherwise.

    """
    return str(item) == str(item)[::-1]


def convert_list_to_int(inlist):
    """Convert a list of digits to a single value.

    Args:
        inlist (list): list of string integers

    Returns:
        int: integer value

    """
    try:
        val = int("".join(map(str, inlist)))
    except ValueError:
        val = 0
    return val


def convert_int_to_list(num):
    """Convert an integer into a list of digits.

    Args:
        num (int): number to convert

    Returns:
        list: list of integers in original number

    """
    return [int(x) for x in str(int(num))]


def convert_list_to_str(li):
    """Convert a list of integers to a string.

    Args:
        li (list): list to convert

    Returns:
        str: string of individual items

    """
    return "".join(map(str,li))


def convert_str_to_list(string):
    """Convert a string to a list of values.

    Args:
        string (str): string to convert

    Returns:
        list: list of values

    """
    return list(string)


def find_all_divisors(n):
    """Return a list of all integers that are divisors of the given n.

    Args:
        n (integer): number to get all divisors for

    Returns:
        list : list of integer divisors

    """
    x = int((n**0.5) // 1)
    i = 2
    lis = [1]
    while i <= x:
        if n % i == 0:
            lis.append(i)
            lis.append(int(n / i))
        i += 1
    return list(set(lis))


def prime_factors(n):
    """Return a list of prime factors of the given number.

    Args:
        n (int): number to get prime factors for

    Returns:
        list: list of prime factors

    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def generate_fibonacci(end):
    """Generate list of fibonacci numbers below end value.

    Args:
        end (int): number to not exceed

    Returns:
        list: list of fibonacci numbers

    """
    x = 1
    y = 2
    fib_list = [1, 2]
    while y < end:
        x, y = y, x + y
        fib_list.append(y)
    return fib_list


def count_of_digits(val):
    """Return a count of the digits of the given integer.

    Args:
        val (int): _description_

    Returns:
        int: count of digits

    """
    # Should use len(convert_int_to_list(val))?
    a = 0
    while val > 0:
        a += 1
        val = val // 10
    return a


def unique_list(li):
    """Return a unique list.

    Args:
        li (list): non-unique list

    Returns:
        list : unique list

    """
    return list(set(li))


def divisible_by_all(num, values):
    """Return whether or not num is divisible by ALL values.

    Args:
        num (int): number to check
        values (list): list of values to check

    Returns:
        bool : boolean answer

    """
    return all(num % ea == 0 for ea in values)


def divisible_by_any(num, values):
    """Return whether or not num is divisible by ANY values.

    Args:
        num (int): number to check
        values (list): list of values to check

    Returns:
        bool : boolean answer

    """
    return any(num % ea == 0 for ea in values)


def get_nth_prime(nth_prime):
    """Get nth prime number.

    Args:
        nth_prime (int): _description_

    Returns:
        int : nth prime number

    """
    prime_list = [2]
    num = 3
    while len(prime_list) < nth_prime:
        # The only numbers you care about are primes, since a prime is not divisible by any other primes.
        if not divisible_by_any(num, prime_list):
            prime_list.append(num)
        num += 2
    return prime_list[-1]


def multiply_list(*args):
    """Multiply a list of values.

    Args:
        *args (list, int): values to multiply

    Returns:
        int : resulting multiplied value

    """
    res = 1
    for arg in args:
        if isinstance(arg, list):
            for ea in arg:
                res *= ea
        else:
            res *= arg
    return res


def add_list(*args):
    """Add a list of values."""
    return sum(args)


def import_2d_array_data(filename):
    """Import a 2D array of data from a CSV file."""
    table = []
    with Path(filename).open()as csvdatafile:
        csvreader = csv.reader(csvdatafile)
        for row in csvreader:
            num_append = list(map(int, row))
            table.append(num_append)
    return table


def import_data(filename):
    """Import data from a CSV file."""
    with Path(filename).open() as csvdatafile:
        return list(csv.reader(csvdatafile))


def import_text_file(file_path):
    with Path(file_path).open("r") as f:
        return f.readlines()


def roundup(numerator, denominator):
    """Round up a number."""
    if numerator % denominator == 0:
        return numerator // denominator
    return (numerator // denominator) + 1


def check_pandigital(value):
    """Check if a number is 1-9 pandigital."""
    return set(value) == {1,2,3,4,5,6,7,8,9}


def check_repeats(value):
    """Check if a number has repeats."""
    return len(set(value)) != len(value)


def flatten_list(nested_list):
    """Flatten a nested list into a single list."""
    return [item for sublist in nested_list for item in sublist]


def calc_factorial(number):
    """Calculate the factorial of a number."""
    if number < 0:
        return -1
    val = 1
    for ea in range(2, number+1):
        val*=ea
    return val


def generate_list_of_circulars(val, return_type=int):
    """Generate a list of circulars of a number. if return_type is int, returns a list of ints, otherwise returns a list of strings."""
    if not isinstance(val, str):
        val = str(val)
    if isinstance(return_type, int):
        return [int(val[i:]) + int(val[:i]) for i in range(len(val))]
    return [val[i:] + val[:i] for i in range(len(val))]


def palindromes_list(max_num):
    """Generate a list of palindromes below max_num."""
    return [ea for ea in range(max_num) if is_palindrome(ea)]


def number_to_base(n, b):
    """Convert a number to a list of digits in a given base.

    Args:
        n (int): number to convert
        b (int): base to convert to

    Returns:
        list: list of digits

    """
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def generate_string_ints_to_n(n):
    if n == 0:
        return ""
    if n == 1:
        return "1"
    prev_string = generate_string_ints_to_n(n-1)
    return prev_string + str(n)


def is_pandigital(s):
    check = "123456789"[:len(s)]
    if len(s) != len(check):
        return False
    if not s.isdigit():
        return False
    return all(digit in s for digit in check)


def get_triangle_number(n):
    return n*(n + 1)/2


def get_pentagonal_number(n):
        return n*(3*n-1)/2


def get_hexagonal_number(n):
        return n*(2*n-1)


def are_permutations(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


def binomial_coefficient(n, k):
    return calc_factorial(n) / (calc_factorial(k) * calc_factorial(n - k))


def xor(a, b):
    return a ^ b

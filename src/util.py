import csv


def is_prime(n):
    """Return True if n is prime. False otherwise.

    Args:
        n (int): number to check

    Returns:
        bool: True if n is prime. False otherwise.

    """
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
    return int("".join(map(str, inlist)))


def convert_int_to_list(num):
    """Convert an integer into a list of digits.

    Args:
        num (int): number to convert

    Returns:
        list: list of integers in original number

    """
    return [int(x) for x in str(int(num))]


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
    """Provide a list of values to multiply. Multiplies all provided numbers together.

    Returns:
        int : resulting multiplied value

    """
    res = 1
    if isinstance(args[0], list):
        for ea in args[0]:
            res *= ea
    else:
        for ea in args:
            res *= ea
    return res


def import_2d_array_data(filename):
    table = []
    with open(filename) as csvdatafile:
        csvreader = csv.reader(csvdatafile)
        for row in csvreader:
            num_append = list(map(int, row))
            table.append(num_append)
    return table


def import_data(filename):
    with open(filename) as csvdatafile:
        return list(csv.reader(csvdatafile))


def roundup(numerator, denominator):
    if numerator % denominator == 0:
        return numerator // denominator
    return (numerator // denominator) + 1

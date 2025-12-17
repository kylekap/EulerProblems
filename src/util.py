import csv
from pathlib import Path

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}


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
    return "".join(map(str, li))


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


def count_of_digits_alt(val):
    """Return a count of the digits of the given integer."""
    return len(str(val))


def sum_digits_powers(number, power):
    return sum(int(ea) ** power for ea in str(number))


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
    with Path(filename).open() as csvdatafile:
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
    return set(value) == {1, 2, 3, 4, 5, 6, 7, 8, 9}


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
    for ea in range(2, number + 1):
        val *= ea
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
    prev_string = generate_string_ints_to_n(n - 1)
    return prev_string + str(n)


def is_pandigital(s):
    check = "123456789"[: len(s)]
    if len(s) != len(check):
        return False
    if not s.isdigit():
        return False
    return all(digit in s for digit in check)


def get_triangle_number(n):
    return n * (n + 1) / 2


def get_square_number(n):
    return n * n


def get_pentagonal_number(n):
    return n * (3 * n - 1) / 2


def get_hexagonal_number(n):
    return n * (2 * n - 1)


def get_heptagonal_number(n):
    return n * (5 * n - 3) / 2


def get_octagonal_number(n):
    return n * (3 * n - 2)


def are_permutations(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


def binomial_coefficient(n, k):
    return calc_factorial(n) / (calc_factorial(k) * calc_factorial(n - k))


def xor(a, b):
    return a ^ b


def check_triangular(n):
    return (8 * n + 1) ** 0.5 % 1 == 0


def check_square(n):
    return n**0.5 % 1 == 0


def check_pentagonal(n):
    return (24 * n + 1) ** 0.5 % 1 == 0


def check_hexagonal(n):
    return (8 * n + 1) ** 0.5 % 1 == 0


def check_heptagonal(n):
    return (40 * n + 9) ** 0.5 % 1 == 0


def check_octagonal(n):
    return (12 * n + 1) ** 0.5 % 1 == 0


def eulers_totient(n):
    """Calculate Euler's Totient function for a given integer n."""
    if n == 0:
        return 0
    result = n
    for p in set(prime_factors(n)): # Use the formula: φ(n) = n * Π(1 - 1/p) for each distinct prime factor p of n
        result *= (1 - 1 / p)
    return int(result)


def gcd(a, b):
    """Euclidean algorithm for gcd.

    The basic Euclidean algorithm is based on the principle that the GCD of two numbers does not change if the larger number
    is replaced by its remainder when divided by the smaller number. The algorithm stops when the remainder is zero.
    """
    while b: #While b is not zero
        a, b = b, a % b #Keep replacing a with b and b with a % b (moving down the chain)
    return a


def alt_gcd(a, b):
    """Alternate gcd function that uses Euclid's algorithm."""
    if b == 0:
        return a
    return alt_gcd(b, a % b)


def reduce_fraction(numerator, denominator):
    """Reduce a fraction to its simplest form."""
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor


def factorial_digits(n):
    """Return the sum of the factorials of the digits of n."""
    fact = {
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
        0: 1,
        } #Precomputed factorials of digits 0-9
    return sum(fact.get(int(digit)) for digit in str(n))


def triangle_check(a, b, c):
    """Check if a, b, and c form a Pythagorean triple."""
    return a**2 + b**2 == c**2


def euclids_formula(m,n):
    a = m**2 - n**2 # Pythagorean triple, a^2 + b^2 = c^2. a = m^2 - n^2
    b = 2*m*n # b = 2mn
    c = m**2 + n**2 # c = m^2 + n^2
    return a, b, c


def continued_fraction_sqrt(c):
    """Compute the continued fraction of sqrt(c) using integer arithmetic.

    Modified from From wikipedia (https://en.wikipedia.org/wiki/Integer_square_root#continued_fraction_sqrt_Python).
    Returns [] if c is a perfect square, otherwise returns the period of the continued fraction.
    """
    a0 = int(c**0.5) # Get the whole number start

    # Perfect square: return period empty
    if a0**2 == c:
        return []

    m = 0
    d = 1
    a = a0
    period = []
    seen = set()

    while True:
        m_next = d * a - m
        d_next = (c - m_next * m_next) // d
        a_next = (a0 + m_next) // d_next

        if (m_next, d_next, a_next) in seen:
            break

        seen.add((m_next, d_next, a_next))
        period.append(a_next)
        m, d, a = m_next, d_next, a_next

    return a0, period


def pell(original_value):
    """Return numerator & denominator for the fundamental solution of Pell's equation for given d.

    Pell's equation is x^2 - d*y^2 = 1.
    """
    p, k, x1, y = 1, 1, 1, 0
    int_sqrt_d = int(original_value**0.5)
    if int_sqrt_d**2 == original_value: # d is a square
        return int_sqrt_d, None
    while k != 1 or y == 0:
        p = k * ((p//k) + 1) - p
        p-= ((p - int_sqrt_d)//k) * k
        x1, y = (p*x1 + original_value * y)//abs(k), (p*y + x1)//abs(k)
        k = (p*p - original_value)//k
    return x1, y


def sqrt_by_subtraction(number, precision):
    """Francis Jarvis method to calculate square root of an integer."""
    a, b = 5*number, 5
    while len(str(b)) < precision+3:
        if a >= b:
            a,b = a-b, b+10
        else:
            a, b = a*100, (b-b%10)*10+b%10
    return str(b)[:precision]


def generate_2d(h, w, fill_value=0):
    return [[fill_value for x in range(w)] for y in range(h)]


def sum_2d(matrix):
    return sum([sum(row) for row in matrix])

def flatten_2d(matrix):
    return [item for row in matrix for item in row]

def return_matrix_value(matrix, coordinate):
    return matrix[coordinate[0]][coordinate[1]]

def set_matrix_value(matrix, coordinate, value):
    matrix[coordinate[0]][coordinate[1]] = value


def modified_dijkstra(matrix, start=(0,0), destination=(0,0)):
    size = len(matrix)
    infinity = sum_2d(matrix) + 1 # Bigger than any of the searches
    unvisited = [(row, col) for row in range(size) for col in range(size)]
    distances = generate_2d(size, size, infinity)
    set_matrix_value(distances, start, return_matrix_value(matrix, start))
    while return_matrix_value(distances, destination) == infinity:
        current = min(unvisited, key=lambda node: return_matrix_value(distances, node))
        for neighbor in [(current[0]-1, current[1]), # up
                         (current[0]+1, current[1]), # down
                         (current[0], current[1]-1), # left
                         (current[0], current[1]+1), # right
                         ]:
            if neighbor in unvisited: # If neighbor is unvisited, this will also serve to make sure we only check cells that are actually in the matrix
                set_matrix_value(distances,
                                      neighbor,
                                      min(return_matrix_value(distances, neighbor), return_matrix_value(distances, current) + return_matrix_value(matrix, neighbor)))
        unvisited.remove(current) # We've visited it now
    return return_matrix_value(distances, destination) # Return the final value


def top_x_from_dict(num_values, my_dict):
    return dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:num_values])


def print_dict(di):
    for k, v in di.items():
        print(f"{k}: {v}")


def print_matrix(matrix):
    for row in matrix:
        print(row)


def roman_numeral_to_int(s):
    li = [roman_numerals[x] for x in s]
    tot = 0
    for i in range(len(li)):
        if i < len(li) - 1 and li[i] < li[i + 1]:
            tot -= li[i]
        else:
            tot += li[i]
    return tot


def int_to_roman_numeral(n):
    roman = ""
    for letter, value in dict(sorted(roman_numerals.items(), key=lambda item: item[1], reverse=True)).items():
        while n >= value:
            n -= value
            roman += letter
    return roman


def pythagorean_triples_under(k):
    max_m = (-1 + (k*2+1)**0.5)/2
    for m in range(2, int(max_m)): # Pythagorean triples
        for n in range(1, m):
            if m*m+n*n > k:
                break
            if gcd(m,n) == 1:
                yield m*m-n*n,2*m*n,m*m+n*n


def area_of_triangle(point1=(0,0), point2=(0,0), point3=(0,0)):
    """Calculate the area of a triangle given three points."""
    return abs(point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1])) / 2


def check_point_in_triangle(point1=(0,0), point2=(0,0), point3=(0,0), point=(0,0)):
    """Check if a point is inside a triangle given three points."""
    # If the the three triangles formed by using the point in the coordinates have areas totaling the area of the triangle, then the point is in the triangle. If it's bigger, it's outside.
    return area_of_triangle(point1, point2, point3) == area_of_triangle(point1, point2, point) + area_of_triangle(point1, point, point3) + area_of_triangle(point, point2, point3)


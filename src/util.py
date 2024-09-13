import csv
import math


def is_prime(n):
    if n in (2, 3):
        return True
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def prime_list(n):
    prime = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if prime[i]:
            prime[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2]+[i for i in range(3,n,2) if prime[i]]


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def convert_list_to_int(inlist):
    return int("".join(map(str, inlist)))


def convert_int_to_list(num):
    return [int(x) for x in str(num)]


def find_all_divisors(n):
    x = math.floor(n**0.5)
    i = 2
    lis = [1]
    while i <= x:
        if n%i == 0:
            lis.append(str(i))
            lis.append(str(int(n/i)))
        i += 1
    return lis


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
    x = 1
    y = 2
    fib_list = [1, 2]
    while y < end:
        x,y = y, x+y
        fib_list.append(y)
    return fib_list


def count_of_digits(val):
    a = 0
    while val > 0:
        a += 1
        val = val//10
    return a


def unique_list(li):
    return list(set(li))


def divisible_by_all(num, values):
    return all(num % ea == 0 for ea in values)


def divisible_by_any(num, values):
    return any(num % ea == 0 for ea in values)


def get_nth_prime(nth_prime):
    prime_list = [2]
    num = 3
    while len(prime_list) < nth_prime:
        #The only numbers you care about are primes, since a prime is not divisible by any other primes.
        if not divisible_by_any(num, prime_list):
            prime_list.append(num)
        num+=2
    return prime_list


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
            num_append = list(map(int,row))
            table.append(num_append)
    return table

def import_data(filename):
    with open(filename) as csvdatafile:
        return list(csv.reader(csvdatafile))

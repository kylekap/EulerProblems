import math

def is_prime(n):
    if n == 2 or n==3:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def prime_list(n): 
    prime = [True]*n
    for i in range(3,int(n**0.5)+1,2):
        if prime[i]:
            prime[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2]+[i for i in range(3,n,2) if prime[i]]


def is_palindrome(n):
    val = str(n)
    if(val == val[::-1]):
        return True
    else:
        return False


def convert_list_to_int(inlist): 
    res = int("".join(map(str, inlist)))   
    return res


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
    for ea in values:
        if num % ea != 0:
            return False
    return True


def divisible_by_any(num, values):
    for ea in values:
        if num % ea ==0:
            return True
    return False


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
    """Provide a list of values to multiply. Multiplies all provided numbers together

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

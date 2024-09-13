import util


def problem1():
    """Problem 1 Euler.

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below .
    """
    return sum([ea for ea in range(1000) if (ea%3 == 0 or ea%5 == 0)])

def problem2():
    """Problem 2 Euler.

    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1,2,3,5,8,13,21,34,55,89...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    li = util.generate_fibonacci(4000000)
    return sum([ea for ea in li if ea % 2 ==0])

def problem3(num=600851475143):
    """Problem 3 Euler.

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    return max(util.prime_factors(num))

def problem4():
    """Problem 4 Euler.

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max([ea_1*ea_2 for ea_1 in range(999,100,-1) for ea_2 in range(999,100,-1) if util.is_palindrome(ea_1*ea_2)])

def problem5():
    """Euler Problem 5.

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    i = 2520 # Gave a starting point
    vals = list(range(1,21))
    while True:
        i+= 2520 #Gunna have to also be divisible by this
        if util.divisible_by_all(i, vals):
            return i

def problem6():
    """Euler Problem 6.

    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    def sum_of_squares(li):
        val = 0
        for ea in li:
            val += ea*ea
        return val
    a = sum(range(1,101))**2
    b = sum_of_squares(range(1,101))
    return a-b

def problem7(num=10001):
    """Euler Problem 7.

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10,001st prime number?
    """
    i = 2
    li = []

    while True:
        if util.is_prime(i):
            li.append(i)
            if len(li) == num:
                return li[-1]
        i+=1

def problem7_alt(num=10001):
    """Euler Problem 7.

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10,001st prime number?
    """
    def get_nth_prime(nth_prime):
        prime_list = [2]
        num = 3
        while len(prime_list) < nth_prime:
            #The only numbers you care about are primes, since a prime is not divisible by any other primes.
            if not util.divisible_by_any(num, prime_list):
                prime_list.append(num)
            num+=2
        return prime_list

    return get_nth_prime(num)[-1]

def problem8(num=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, consecutive=13):
    """Euler Problem 8.

    The four adjacent digits in the 1000-digit number that have the greatest product are 9 times 9 times 8 times 9 = 5832.
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
    """
    li = [int(x) for x in str(num)]
    highest = 0
    for i in range(1,len(li)-consecutive):
        highest = max(util.multiply_list(li[i:i+consecutive]), highest)
    return highest

def problem9(desired_sum):
    """Euler Problem 9.

    A Pythagorean triplet is a set of three natural numbers, a<b<c, for which a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product a*b*c
    """
    a,b,c = 1,2,3
    for a in range(1,desired_sum//3):
        for b in range(a,desired_sum//2):
            for c in range(max(b,desired_sum//3),desired_sum-b-a+1):
                if a**2 + b**2 == c**2 and a+b+c==desired_sum:
                    return a*b*c
    return None

def problem10():
    """Euler Problem 10.

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    def prime_list(n):
        prime = [True]*n
        for i in range(3,int(n**0.5)+1,2):
            if prime[i]:
                prime[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        return [2]+[i for i in range(3,n,2) if prime[i]]
    return sum(prime_list(2000000))


def problem11():
    def get_rows(grid, adj):
        li = []
        for row_num in range(len(grid)):
            for col_num in range(len(grid[row_num])-adj+1):
                temp = [grid[row_num][col_num+offset] for offset in [0,1,2,3]]
                li.append(temp)
        return li

    def get_cols(grid,adj):
        li = []
        for row_num in range(len(grid)-adj+1):
                for col_num in range(len(grid[row_num])):
                    temp = [grid[row_num+offset][col_num] for offset in [0,1,2,3]]
                    li.append(temp)
        return li

    def get_diags(grid, adj):
        li = []
        for row_num in range(len(grid)-adj+1):
            for col_num in range(len(grid[row_num])-adj+1):
                temp = [grid[row_num+offset][col_num+offset] for offset in [0,1,2,3]]
                li.append(temp)
            for col_num in range(adj-1, len(grid[row_num])):
                temp = [grid[row_num+offset][col_num-offset] for offset in [0,1,2,3]]
                li.append(temp)
        return li

    grid = util.import_data("data/SumGrid.csv")
    adj = 4
    li = get_rows(grid, adj)
    li+= get_cols(grid, adj)
    li+= get_diags(grid, adj)

    max_value = 0
    for line in li:
        max_value = max(max_value, util.multiply_list(line))
    return max_value

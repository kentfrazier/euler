# Project Euler - Problem 10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

from Problem003 import next_prime

def prime_list(limit):
    primes = range(2,limit)

    i = 0
    while i <= len(primes) - 1:
        
        num = primes[i] * 2

        while num < limit:

            try:
                del primes[primes.index(num)]
            except ValueError:
                pass

            num += primes[i]
        
        i += 1

    return primes

def sum_of_primes(limit):
    return sum(prime_list(limit))


def prime_list2(limit):
    primes = set(range(2,limit))

    i = 0
    while i <= len(primes) - 1:
        
        num = primes[i] * 2

        while num < limit:

            primes.remove(num)

            num += primes[i]
        
        i += 1

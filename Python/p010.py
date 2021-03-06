# Project Euler - Problem 10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
import math
try:
    import psyco
    psyco.full()
except ImportError:
    pass

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
    return sum(prime_list3(limit))

# This version doesn't really work because sets are not indexable
# def prime_list2(limit):
#     primes = set(range(2,limit))
# 
#     i = 0
#     while i <= len(primes) - 1:
#         
#         num = primes[i] * 2
# 
#         while num < limit:
# 
#             primes.remove(num)
# 
#             num += primes[i]
#         
#         i += 1

def prime_sieve(limit):
    primes = dict([(i, True) for i in range(2,limit)])
    test_max = math.sqrt(limit)

    for num in sorted(primes.keys()):
        if num > test_max: break

        if not primes[num]: continue

        multiple = num ** 2

        while multiple < limit:
            primes[multiple] = False
            multiple += num

    return [ n for n in sorted(primes.keys()) if primes[n] ]

prime_list3 = prime_sieve

if __name__ == "__main__":
    print sum_of_primes(2000000)

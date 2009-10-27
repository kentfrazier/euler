from itertools import ifilter, count
from math import floor, sqrt, ceil

low_prime_set = set([2,3,5])
mod30_set = set([1,7,11,13,17,19,23,29])

_prime_list = [2,3]

def is_potential_prime(n):
    return n % 30 in mod30_set

def potential_primes(start=2, limit=None):
    
    def candidates(start=1):
        for i in count(start):
            n = 6 * i

            yield n - 1
            yield n + 1

    for i in [ n for n in [2,3] if n >= start and n < limit ]:
        yield i
            
    for candidate in ifilter(is_potential_prime, candidates(int(ceil(start / 6.)))):
        if limit is not None and candidate > limit:
            return
        yield candidate

def is_really_prime(n):
    for pprime in potential_primes(limit=sqrt(n)):
        if n % pprime == 0:
            return False
    return True

def is_prime(n):
    if n == 1:
        return False
    if n in low_prime_set:
        return True
    return is_potential_prime(n) and is_really_prime(n)

def prime_sieve(limit):
    primes = dict([(i, True) for i in range(2,limit)])
    test_max = sqrt(limit)

    for num in sorted(primes.keys()):
        if num > test_max: break

        if not primes[num]: continue

        multiple = num ** 2

        while multiple < limit:
            primes[multiple] = False
            multiple += num

    return [ n for n in sorted(primes.keys()) if primes[n] ]

def primes(start=2, limit=None):
    for prime in _prime_list:
        if limit is not None and prime > limit:
            return
        if prime >= start:
            yield prime
    for prime in ifilter(is_really_prime, potential_primes(start=_prime_list[-1])):
        _prime_list.append(prime)
        if limit is not None and prime > limit:
            return
        if prime >= start:
            yield prime


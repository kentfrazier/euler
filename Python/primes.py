from itertools import ifilter, count
from math import sqrt, ceil

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
            
    for candidate in ifilter(is_potential_prime,
                             candidates(int(ceil(start / 6.)))):
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

from math import log
def prime_bit_sieve(limit):
    # this is fun and works but is super slow compared to the dict approach
    # above. I wonder if that is just Python or if the same is true in C
    primes = int('0b' + '1' * limit, 2)
    primes ^= 3 # 0 and 1 are not prime
    test_max = sqrt(limit)

    bit_limit = 1 << (limit + 1)
    for num in xrange(2, limit):
        if num > test_max:
            break

        if not primes & (1 << num):
            continue

        mask = 0
        while mask < bit_limit:
            mask += 1
            mask <<= num

        mask <<= num # don't blot out the prime
        mask = mask
        primes &= ~mask

    return [ i for i in xrange(int(ceil(log(primes, 2))) + 1)
             if primes & (1 << i) ]

def primes(start=2, limit=None):
    for prime in _prime_list:
        if limit is not None and prime > limit:
            return
        if prime >= start:
            yield prime
    for prime in ifilter(is_really_prime,
                         potential_primes(start=_prime_list[-1])):
        _prime_list.append(prime)
        if limit is not None and prime > limit:
            return
        if prime >= start:
            yield prime


# The number 3797 has an interesting property. Being prime itself, it is 
# possible to continuously remove digits from left to right, and remain prime 
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
# left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left 
# to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from Problem032 import render_to_number
from itertools import ifilter, product, count, chain
from math import sqrt

def truncations(number):
    digits = str(number)

    for i in xrange(1,len(digits)):
        yield int(digits[:-i])
        yield int(digits[i:])

def is_truncatable(number):
    if not is_prime(number):
        return False

    if any( not is_prime(trunc) for trunc in truncations(number) ):
        return False

    return True

def potential_primes(limit=None):
    
    def candidates(start=1):
        for i in count(start):
            n = 6 * i

            yield n - 1
            yield n + 1
            
    mod30_set = set([1,7,11,13,17,19,23,29])

    def is_potential(n):
        if n % 30 in mod30_set:
            return True
        return False

    for n in chain([2,3,5],ifilter(is_potential,candidates())):

        if limit and n > limit:
            break

        yield n

    raise StopIteration()

def is_prime(n):
    for pprime in potential_primes(sqrt(n)):
        if n % pprime == 0:
            return False

    return True

def potential_truncatable_primes():
    begin_digits  = (2,3,4,5,7)
    middle_digits = (1,3,7,9)
    end_digits    = (3,7)

    for i in count():
        for num in [ render_to_number(seq) for seq in
                [ (beg,) + mid + (end,)
                    for beg in begin_digits
                    for mid in product(middle_digits, repeat=i)
                    for end in end_digits
                ] ]:
            yield num

def truncatable_primes():
    prime_count = 0
    for prime in ifilter(is_truncatable,
            potential_truncatable_primes()):
        yield prime

        prime_count += 1
        if prime_count >= 11: break

    raise StopIteration()

if __name__ == "__main__":
    trunc_primes = list(truncatable_primes())

    assert( 3797 in trunc_primes )
    assert( len(trunc_primes) == 11 )

    print 'Truncatable Primes:', trunc_primes
    print 'Sum:', sum(trunc_primes)

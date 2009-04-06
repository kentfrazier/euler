# The number 3797 has an interesting property. Being prime itself, it is 
# possible to continuously remove digits from left to right, and remain prime 
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
# left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left 
# to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from Problem010 import prime_list3
from itertools import ifilter

primes = prime_list3(1000000)
prime_set = set(primes)

def truncations(number):
    digits = str(number)

    for i in xrange(1,len(digits)):
        yield int(digits[:-i])
        yield int(digits[i:])

def is_truncatable(number):
    if number not in prime_set:
        return False

    if any( trunc not in prime_set for trunc in truncations(number) ):
        return False

    return True

def truncatable_primes():

    one_digit_primes = set(['2','3','5','7'])

    def is_candidate(number):
        num_str = str(number)

        if len(num_str) < 2: return False

        if not num_str[0] in one_digit_primes and num_str[-1] in one_digit_primes:
            return False

        digits = set([ int(digit) for digit in num_str ])

        if 5 in digits and num_str[0] != '5':
            return False

        if any( d % 2 == 0 for d in digits ):
            return False

        return True

    trunc_primes = []

    for prime in ifilter(is_truncatable,ifilter(is_candidate,primes)):
        if is_candidate(prime):
            if is_truncatable(prime):
                trunc_primes.append(prime)

    return trunc_primes

if __name__ == "__main__":
    trunc_primes = truncatable_primes()

    assert( 3797 in trunc_primes )
    assert( len(trunc_primes) == 11 )

    print 'Truncatable Primes:', trunc_primes
    print 'Sum:', sum(trunc_primes)

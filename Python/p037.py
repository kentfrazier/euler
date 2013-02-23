# The number 3797 has an interesting property. Being prime itself, it is 
# possible to continuously remove digits from left to right, and remain prime 
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to 
# left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left 
# to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from p010 import prime_list3
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
    forbidden_numbers = set(['4','6','8'])

    def is_candidate(number):
        num_str = str(number)

        if len(num_str) < 2: return False

        if not set([num_str[0], num_str[-1]]) < one_digit_primes:
            return False

        digits = set([ digit for digit in num_str ])

        if digits & forbidden_numbers:
            return False

        if '2' in digits and num_str[0] != '2':
            return False

        if '5' in digits and num_str[0] != '5':
            return False

        return True

    trunc_primes = []

    for prime in ifilter(is_truncatable,ifilter(is_candidate,primes)):
        trunc_primes.append(prime)
        if len(trunc_primes) == 11: break

    return trunc_primes

if __name__ == "__main__":
    trunc_primes = truncatable_primes()

    assert( 3797 in trunc_primes )
    assert( len(trunc_primes) == 11 )

    print 'Truncatable Primes:', trunc_primes
    print 'Sum:', sum(trunc_primes)

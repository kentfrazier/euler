# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
# 
# How many circular primes are there below one million?

# from Problem003 import primes, prime_number_list, prime_list
from Problem010 import prime_list3 as prime_list
from collections import deque

def rotations(number, include_original=False):
    digits = deque([ digit for digit in str(number) ])

    rotation_count = len(digits)
    if not include_original:
        rotation_count -= 1

    for c in xrange(rotation_count):
        digits.rotate(1)
        yield int(''.join(digits))

def circular_primes(limit):

    def is_candidate(number):
        digits = [int(digit) for digit in str(number)]

        if len(digits) == 1:
            return True

        if any( d % 2 == 0 for d in digits ):
            return False

        if 5 in digits:
            return False

        return True
        
    primes = prime_list(limit)

    for prime in primes:
        if not is_candidate(prime): continue

        if all( num in primes for num in rotations(prime) ):
            yield prime

if __name__ == "__main__":
    assert( len(list(circular_primes(100))) == 13 )
    assert( list(circular_primes(100)) == [2,3,5,7,11,13,17,31,37,71,73,79,97] )
    print len(list(circular_primes(1000000)))

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
# of each of the digits 0 to 9 in some order, but it also has a rather 
# interesting sub-string divisibility property.
# 
# Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In 
# this way, we note the following:
# 
#     * d_(2)d_(3)d_(4)=406 is divisible by 2
#     * d_(3)d_(4)d_(5)=063 is divisible by 3
#     * d_(4)d_(5)d_(6)=635 is divisible by 5
#     * d_(5)d_(6)d_(7)=357 is divisible by 7
#     * d_(6)d_(7)d_(8)=572 is divisible by 11
#     * d_(7)d_(8)d_(9)=728 is divisible by 13
#     * d_(8)d_(9)d_(10)=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations, ifilter, cycle, izip
from Problem010 import prime_sieve
from Problem032 import render_to_number

def pandigitals(length):
    if length > 10:
        raise Exception('Pandigital number cannot be longer than 10 digits.')

    if length < 10:
        digits = range(1,length+1)
    else:
        digits = range(length)

    for perm in ifilter(lambda x: x[0] != 0, permutations(digits)):
        if perm[0] == 0: continue

        yield render_to_number(perm)

def substring_numbers(number,length,start_index=0):
    num_str = str(number)

    for i in xrange(start_index, 1 + len(num_str) - length):
        yield int(num_str[i:i+length])

def odd_divisible_pandigitals():
    small_primes = prime_sieve(20)

    def sub_divides(number):
        if all( sub % prime == 0 for sub, prime
                in izip(substring_numbers(number,3,1),cycle(small_primes)) ):
            return True
        return False

    for pandigital in ifilter(sub_divides,pandigitals(10)):
        yield pandigital

if __name__ == "__main__":
    curious_pandigitals = list(odd_divisible_pandigitals())
    assert( 1406357289 in curious_pandigitals )

    print curious_pandigitals
    print 'Sum:', sum(curious_pandigitals)

# We shall say that an n-digit number is pandigital if it makes use of all 
# the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital 
# and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

from p010 import prime_list3
from itertools import ifilter
try:
    import psyco
    psyco.full()
except ImportError:
    pass

def is_pandigital(number):
    str_num = str(number)

    digits = set([ int(digit) for digit in str_num ])

    if len(str_num) != len(digits):
        return False # had duplicate digits

    if digits == set(range(1,len(str_num)+1)):
        return True

    return False

def pandigital_primes():
    biggest_pandigital = 7654321
    primes = prime_list3(biggest_pandigital+1)

    for prime in ifilter(is_pandigital, primes):
        yield prime

def largest_pandigital():
    return max(pandigital_primes())

if __name__ == "__main__":
    print largest_pandigital()

# It was proposed by Christian Goldbach that every odd composite number can 
# be written as the sum of a prime and twice a square.
# 
#  9 = 7  + 2*1^(2)
# 15 = 7  + 2*2^(2)
# 21 = 3  + 2*3^(2)
# 25 = 7  + 2*3^(2)
# 27 = 19 + 2*2^(2)
# 33 = 31 + 2*1^(2)
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a 
# prime and twice a square?

from p010 import prime_sieve
from math import sqrt

def smallest_odd_composite():
    def odd_numbers(start=1):
        num = start
        while True:
            yield num
            num += 2

    primes = set(prime_sieve(10000))
    odd_composites = ( i for i in odd_numbers(9)
            if i not in primes and i < 10000)

    for n in odd_composites:
        if any( (n - (2 * base ** 2)) in primes
                for base in xrange(1, (int(sqrt((n-2)/2))+1)) ):
            continue

        return n

if __name__ == "__main__":
    print smallest_odd_composite()

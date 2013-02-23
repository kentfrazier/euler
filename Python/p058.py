# Starting with 1 and spiralling anticlockwise in the following way, 
# a square spiral with side length 7 is formed.
# 
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# 
# It is interesting to note that the odd squares lie along the bottom 
# right diagonal, but what is more interesting is that 8 out of the 
# 13 numbers lying along both diagonals are prime; that is, a ratio 
# of 8/13 approximately equals 62%.
# 
# If one complete new layer is wrapped around the spiral above, a 
# square spiral with side length 9 will be formed. If this process is 
# continued, what is the side length of the square spiral for which 
# the ratio of primes along both diagonals first falls below 10%?

from __future__ import division
from itertools import count

from p049 import is_prime

def interval_gen():
    for i in count(1):
        yield 2 * i

def diagonal_gen():
    value = 1
    yield value
    for interval in interval_gen():
        for i in xrange(4):
            value += interval
            yield value

def diagonal_prime_pct_below(pct):
    diagonals = diagonal_gen()

    prime_count = 0
    diagonal_count = 0

    size = 1
    diagonal = diagonals.next()
    diagonal_count += 1
    if is_prime(diagonal):
        prime_count += 1

    while True:
        size += 2
        for i in xrange(4):
            diagonal = diagonals.next()
            diagonal_count += 1
            if is_prime(diagonal):
                prime_count += 1
        if ( prime_count / diagonal_count ) < pct:
            break
    return size

if __name__ == "__main__":
    print diagonal_prime_pct_below(0.10)

# The fraction ^(49)/_(98) is a curious fraction, as an inexperienced 
# mathematician in attempting to simplify it may incorrectly believe that 
# ^(49)/_(98) = ^(4)/_(8), which is correct, is obtained by cancelling the 
# 9s.
# 
# We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial 
# examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and 
# denominator.
# 
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

from fractions import Fraction
from operator import mul
from functools import reduce

def is_candidate(n, d):
    n_digits = set([ int(digit) for digit in str(n) ])
    d_digits = set([ int(digit) for digit in str(d) ])

    common = n_digits & d_digits
    if len(common) != 1: # no intersection, or too much intersection
        return False
    if 0 in common: # trivial cases
        return False

    if n_digits != common: # necessary to handle repeated digits
        n_digits -= common
    if d_digits != common:
        d_digits -= common

    if 0 in n_digits or 0 in d_digits:
        return False

    if Fraction(n, d) == Fraction(n_digits.pop(),d_digits.pop()):
        return True

    return False

def find_non_trivial_curious_fractions():
    return [ Fraction(n, d) for n in xrange(10,100) 
                            for d in xrange(n+1,100)
                            if is_candidate(n, d) ]

if __name__ == "__main__":
    print reduce(mul, find_non_trivial_curious_fractions()).denominator

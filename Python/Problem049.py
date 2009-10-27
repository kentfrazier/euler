# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
# increases by 3330, is unusual in two ways:
#   (i)  each of the three terms are prime, and, 
#   (ii) each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
# primes, exhibiting this property, but there is one other 4-digit increasing 
# sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this 
# sequence?

from itertools import permutations, ifilter
from Problem037_2 import is_prime as is_really_prime
from Problem037_2 import is_potential_prime

def digit_permutations(n):
    return [ int(''.join(perm)) for perm in permutations(str(n)) ]

low_primes = set([2,3,5])
def is_prime(n):
    if n == 1:
        return False
    if n in low_primes:
        return True
    if not is_potential_prime(n) or not is_really_prime(n):
        return False
    return True

def n_digit_primes(n):
    return ifilter(is_prime, xrange(10**(n-1),10**n))

def is_uniform_seq(seq):
    if all( n == seq[0] for n in seq ):
        return True
    return False

def find_sequences(length=4, num=3):
    already_processed = set()

    for n in n_digit_primes(length):
        if '0' in str(n):
            continue
        if n in already_processed:
            continue

        perms = filter(is_prime,set(digit_permutations(n)))

        already_processed |= set(perms)

        if len(perms) < num:
            continue
        
        possibles = set( tuple(sorted(seq)) for seq in permutations(perms, num) )

        for seq in possibles:
            if is_uniform_seq([ seq[i] - seq[i-1] for i in xrange(1,len(seq)) ]):
                yield seq

if __name__ == "__main__":
    for seq in find_sequences(4,3):
        if seq[0] != 1487:
            print ''.join(str(n) for n in seq)

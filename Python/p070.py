"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used
to determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, phi(9)=6.  The number 1 is considered to be
relatively prime to every positive number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and
the ratio n/phi(n) produces a minimum.
"""

from p069 import totient, factor_list

def totient_perms(limit):
    for num in xrange(2, limit):
        totient_val = totient(num)
        if sorted(str(num)) == sorted(str(totient_val)):
            yield num, totient_val

def min_totient_ratio(limit):
    def key_fn(item):
        return float(item[0]) / item[1]
    return min(totient_perms(limit), key=key_fn)[0]

def is_totient_perm(num):
    return sorted(str(num)) == sorted(str(totient(num)))

from primes import is_prime, primes

def candidates(count, limit):
    root = int(limit ** (1. / count))
    if count == 1:
        for num in xrange(root - (1 - (root % 2)), 2, -2):
            if is_prime(num):
                yield [num]
        yield [2]
    else:
        for prime in primes(start=root, limit=limit):
            rest = candidates(count - 1, limit // prime)
            for nums in rest:
                yield [prime] + nums


from math import sqrt
def possibilities(limit):
    for prime in primes(limit=sqrt(limit)):
        val = prime ** 2
        if is_totient_perm(val):
            return val
    for prime in primes(limit=limit ** (1./3)):
        val = prime ** 3
        if is_totient_perm(val):
            return val

def main():
    limit = 10 ** 7
    factor_list.factor_to(limit)
    print min_totient_ratio(limit)

if __name__ == "__main__":
    main()

# different approach: perhaps find the number with the largest and least number
# of prime factors, which will result in a large totient

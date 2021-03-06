# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 * 7
# 15 = 3 * 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 
# 644 = 2^2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19
# 
# Find the first four consecutive integers to have four distinct primes 
# factors. What is the first of these numbers?

from p003 import primes
from collections import defaultdict
from itertools import islice, izip, count
from operator import mul
from functools import reduce

class FactorList(defaultdict):
    def __init__(self, limit=0):
        super(FactorList, self).__init__(list)
        self._cached = {}
        self.limit = 0
        self.factor_to(limit)

    def factor_to(self, limit):
        if limit <= self.limit:
            return

        start_value = self.limit

        for num in xrange(2,limit):
            if num in self:
                continue

            multiple = max([num, start_value - (start_value % num)])
            while True:
                multiple += num
                if multiple > limit:
                    break
                if multiple not in self:
                    self[multiple].extend([num, multiple // num])

        self.limit = limit

    def is_prime(self, number):
        if number > self.limit:
            self.factor_to(number)
        
        if number not in self:
            return True
        return False

    def factor(self, number):
        if number in self._cached:
            return self._cached[number]

        if number > self.limit:
            self.factor_to(number*2)

        if self.is_prime(number):
            return [number]

        all_factors = self[number]
        prime_factors = [all_factors[0]]

        for factor in all_factors[1:]:
            prime_factors.extend(self.factor(factor))
        prime_factors.sort()

        self._cached[number] = prime_factors
        return prime_factors

def first_n_to_n_prime_factors(n):
    start_value = reduce(mul, islice(primes(),0,n))

    factors = FactorList(10**(n+1))

    for seq in izip(*[ count(start_value+i) for i in xrange(n) ]):
        if all( len(set(factors.factor(num))) == n for num in seq ):
            return seq

if __name__ == "__main__":
    print first_n_to_n_prime_factors(4)[0]

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

from Problem003 import primes
from collections import defaultdict
from itertools import dropwhile, islice, izip, count
from operator import mul
from functools import reduce

class Factor_List(defaultdict):
    def __init__(self, limit=0):
        super(Factor_List, self).__init__(list)
        self.limit = 0
        self.factor_to(limit)

    def factor_to(self, limit):
        if limit <= self.limit:
            return

        start_value = self.limit

        for num in xrange(2,limit):
            if num in self:
                continue

            multiple = num + start_value - (start_value % num)
            while True:
                multiple += num

                if multiple > limit: break

                if multiple not in self:
                    self[multiple] += [num, multiple // num]

        self.limit = limit

    def is_prime(self, number):
        if number > self.limit:
            self.factor_to(number)
        
        if number not in self:
            return True
        return False

    def factor(self, number):
        if number > self.limit:
            self.factor_to(number)

        if self.is_prime(number):
            return [number]

        return sorted(reduce(lambda x, y: x + y, 
                [ self.factor(n) for n in self[number] ]))

def first_n_to_n_prime_factors(n):
    start_value = reduce(mul, islice(primes(),0,n))

    factors = Factor_List(start_value * 3)

    for seq in izip(*[ count(start_value+i) for i in xrange(n) ]):
        if all( len(set(factors.factor(num))) == n for num in seq ):
            return seq

# TODO: Work out how to make this more efficient to solve the problem
# currently won't even solve for 3 in a reasonable amount of time

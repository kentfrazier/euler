"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used
to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, phi(9)=6.

n   Relatively Prime    phi(n)  n/phi(n)
2   1                   1       2
3   1,2                 2       1.5
4   1,3                 2       2
5   1,2,3,4             4       1.25
6   1,5                 2       3
7   1,2,3,4,5,6         6       1.1666...
8   1,3,5,7             4       2
9   1,2,4,5,7,8         6       1.5
10  1,3,7,9             4       2.5

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""

from operator import mul

from p047 import FactorList

factor_list = FactorList()

def totient(num):
    if num == 1:
        return 1 # special case
    factors = set(factor_list.factor(num))
    coprime_count = num * reduce(mul, [1 - (1. / prime) for prime in factors])
    return int(round(coprime_count))

def totient_ratio(num):
    return float(num) / totient(num)

def max_n_over_phi_n(limit):
    max_num = None
    max_ratio = 0
    for num in xrange(2, limit + 1):
        ratio = totient_ratio(num)
        if ratio > max_ratio:
            max_num = num
            max_ratio = ratio
    return max_num

def main():
    assert(max_n_over_phi_n(10) == 6)
    print max_n_over_phi_n(1000000)

if __name__ == "__main__":
    main()

"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d \u2264 8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.
"""

from fractions import Fraction

def find_next_lowest(value, limit):
    candidates = set([value])
    for denominator in xrange(2, limit + 1):
        candidates.add(Fraction(int(denominator * value), denominator))
    candidates.remove(value)
    return sorted(candidates, reverse=True)[0]

def test():
    assert(find_next_lowest(Fraction(3, 7), 8) == Fraction(2, 5))

def main():
    # This solves it, but it took 10 minutes on the netbook
    print find_next_lowest(Fraction(3, 7), 1000000)

if __name__ == '__main__':
    test()
    main()

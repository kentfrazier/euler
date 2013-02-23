"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for
d <= 1,000,000?
"""

def reduced_proper_fractions(limit):
    # initialize counts with each index holding the total number of proper
    # fractions for a denominator equal to i + 1 (which will equal i)
    counts = range(limit)

    # for each denominator, find all multiples and subtract the number of
    # remaining distinct proper fractions for the denominator for each
    # multiple found
    for i in xrange(1, limit):
        denominator = i + 1
        multiple = denominator * 2
        while multiple <= limit:
            counts[multiple - 1] -= counts[i]
            multiple += denominator

    return sum(counts)

def test():
    assert(reduced_proper_fractions(8) == 21)

def main():
    print reduced_proper_fractions(1000000)

if __name__ == '__main__':
    test()
    main()

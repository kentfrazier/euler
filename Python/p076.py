"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""

from itertools import groupby
from operator import itemgetter

def list_sums(num, maximum=None):
    if num == 1:
        return[(1,)]

    sums = []

    if maximum is None:
        start = num - 1
    else:
        start = min([maximum, num - 1])
    for n in xrange(start, 0, -1):
        complement = num - n
        if n >= complement:
            sums.append((n, complement))
        if complement == 1:
            continue
        for sum in list_sums(num - n, maximum=n):
            sums.append((n,) + sum)
    return sums

def dist_analysis(num):
    dist = [(el[0], len(list(el[1]))) for el
            in groupby(list_sums(num), key=itemgetter(0))]
    return dist

def count_sums(num):
    def iter(n, inner=False, limit=None):
        total = 0
        if limit is None:
            limit = n
        for m in range(2, limit):
            if inner:
                count = n - m
            else:
                count = n - (2 * m) + 1
            while count > 0:
                total += count
                total += iter(count, inner=True, limit=m)
                count -= m
        return total
    return num - 1 + iter(num)

def main():
    assert(count_sums(5) == 6)
    print count_sums(100)

if __name__ == "__main__":
    main()

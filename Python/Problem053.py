# There are exactly ten ways of selecting three from five, 12345:
# 
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# 
# In combinatorics, we use the notation, ^(5)C_(3) = 10.
# 
# In general,
# ^(n)C_(r) = n! / r!(n-r)!
# 	,where r <= n, n! = nx(n-1)x...x3x2x1, and 0! = 1.
# 
# It is not until n = 23, that a value exceeds one-million: 
# ^(23)C_(10) = 1144066.
# 
# How many, not necessarily distinct, values of  ^(n)C_(r), for 1 <= n <= 100,
# are greater than one-million?

from math import factorial

def ways(n, r):
    return factorial(n) / ( factorial(r) * factorial(n - r) )

def exceeding(limit):
    return [ (n, r) for n in xrange(1,101)
                    for r in xrange(1,n+1) if ways(n, r) > limit ]

if __name__ == "__main__":
    print len(exceeding(1000000))

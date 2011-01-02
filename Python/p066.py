"""
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2x2^2 = 1
2^2 - 3x1^2 = 1
9^2 - 5x4^2 = 1
5^2 - 6x2^2 = 1
8^2 - 7x3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
from itertools import count, cycle

from p064 import get_sqrt_continued_fraction
from p065 import convergent_point

class PerfectSquareError(Exception):
    pass

def test(d, x, y):
    return x**2 - d * y**2 == 1

def solve(d):
    integer, period = get_sqrt_continued_fraction(d)

    if len(period) == 0:
        raise PerfectSquareError('d cannot be a perfect square!')

    for i in count(1):
        frac = convergent_point(integer, cycle(period), i)
        x = frac.numerator
        y = frac.denominator
        if test(d, x, y):
            return (x, y)

def max_minimal_solution(limit):
    x_values = {}
    for d in xrange(2, limit + 1):
        try:
            x, y = solve(d)
        except PerfectSquareError:
            continue
        x_values[d] = x

    return max(x_values.keys(), key=x_values.get)

def main():
    assert(max_minimal_solution(7) == 5)
    print max_minimal_solution(1000)

if __name__ == "__main__":
    main()

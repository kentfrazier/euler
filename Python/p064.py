"""
All square roots are periodic when written as continued fractions and can be
written in the form:
sqrt(N) = a0 + (1 / a1 + (1 / a2 + (1 / a3 + ...)))

For example, let us consider sqrt(23):
sqrt(23) = 4 + sqrt(23) - 4
    = 4 + (1 / (1 / (sqrt(23) - 4)))
    = 4 + (1 / (1 + ((sqrt(23) - 3) / 7)))

If we continue we would get the following expansion:
sqrt(23) = 4 + (1 / (1 + (1 / (3 + (1 / (1 + (1 / (8 + ...))))))))

The process can be summarised as follows:
a0 = 4, 1 / (sqrt(23) - 4) = (sqrt(23) + 4) / 7 = 1 + ((sqrt(23) - 3) / 7)
a1 = 1, 7 / (sqrt(23) - 3) = 7 * (sqrt(23) + 3) / 14 = 3 + ((sqrt(23) - 3) / 2)
a2 = 3, 2 / (sqrt(23) - 3) = 2 * (sqrt(23) + 3) / 14 = 1 + ((sqrt(23) - 4) / 7)
a3 = 1, 7 / (sqrt(23) - 4) = 7 * (sqrt(23) + 4) / 7 = 8 + sqrt(23) - 4
a4 = 8, 1 / (sqrt(23) - 4) = (sqrt(23) + 4) / 7 = 1 + ((sqrt(23) - 3) / 7)
a5 = 1, 7 / (sqrt(23) - 3) = 7 * (sqrt(23) + 3) / 14 = 3 + ((sqrt(23) - 3) / 2)
a6 = 3, 2 / (sqrt(23) - 3) = 2 * (sqrt(23) + 3) / 14 = 1 + ((sqrt(23) - 4) / 7)
a7 = 1, 7 / (sqrt(23) - 4) = 7 * (sqrt(23) + 4) / 7 = 8 + sqrt(23) - 4

It can be seen that the sequence is repeating. For conciseness, we use the
notation sqrt(23) = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:

sqrt(2)  = [1;(2)],         period=1
sqrt(3)  = [1;(1,2)],       period=2
sqrt(5)  = [2;(4)],         period=1
sqrt(6)  = [2;(2,4)],       period=2
sqrt(7)  = [2;(1,1,1,4)],   period=4
sqrt(8)  = [2;(1,4)],       period=2
sqrt(10) = [3;(6)],         period=1
sqrt(11) = [3;(3,6)],       period=2
sqrt(12) = [3;(2,6)],       period=2
sqrt(13) = [3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
"""

from itertools import count

def get_sqrt_continued_fraction(num):
    # This is sort of ugly. I don't want to use int(sqrt()), but I feel like
    # there is a smarter way to get the integer portion of the square root.
    # Surprisingly, this is almost as efficient as int(sqrt())
    for i in count(0):
        if i ** 2 > num:
            whole = i - 1
            break

    def process(numer, denom_mod):
        """
        Processes current values and returns next set.

        In the equation:
            numer / (sqrt(num) - denom_mod)
        it will extract the next number in the continued fraction and return
        the remainder as a fraction in the same form, with new numer and
        denom_mod
        """
        new_numer = (num - denom_mod ** 2) / numer
        top_sum = whole + denom_mod
        next_number = top_sum // new_numer
        new_denom_mod = (next_number * new_numer) - denom_mod
        return (next_number, new_numer, new_denom_mod)

    period = []

    processed = set([])

    numer = 1
    denom = whole
    while (numer, denom) not in processed:
        # when we hit a pair we have already processed, we know we have
        # hit the repeating point in the fraction
        processed.add((numer, denom))
        try:
            digit, numer, denom = process(numer, denom)
        except ZeroDivisionError:
            break # perfect square
        period.append(digit)

    return (whole, tuple(period))

def count_odd_periods(limit):
    odd = 0

    for num in xrange(1, limit + 1):
        whole, period = get_sqrt_continued_fraction(num)
        if len(period) & 1:
            odd += 1

    return odd

def main():
    assert(count_odd_periods(13) == 4)

    print count_odd_periods(10000)

if __name__ == "__main__":
    main()

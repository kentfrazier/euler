"""
Comparing two numbers written in index form like 2**11 and 3**7 is not
difficult, as any calculator would confirm that 2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

from math import (
    ceil,
    log,
)

class BigExp(object):

    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

        base_log2 = log(base, 2)
        self.num_binary_digits = int(ceil(base_log2 * exponent))
        if base_log2 % 1 == 0:
            self.num_binary_digits += 1
        # As it turns out, this could have been solved easier had I just
        # calculated log(base) * exponent, which would have captured total
        # value rather than just the number of digits. I am still pretty
        # proud of my solution, but I over-complicated things.

    def __cmp__(self, other):
        digit_diff = self.num_binary_digits - other.num_binary_digits
        if digit_diff:
            return digit_diff

        # Hope we almost never hit this
        return cmp(self.base**self.exponent,
                   other.base**other.exponent)

    def __repr__(self):
        return 'BigNum({base}, {exponent})'.format(
            base=self.base,
            exponent=self.exponent,
        )

def test_num_binary_digits():
    for base in xrange(1, 501):
        for exponent in xrange(1, 501):
            bn_len = BigExp(base, exponent).num_binary_digits
            real_len = len(bin(base**exponent)[2:])
            try:
                assert(bn_len == real_len)
            except AssertionError:
                print base, exponent, bn_len, real_len
                raise

def main():
    nums = []
    with open('base_exp.txt', 'r') as f:
        for line in f:
            nums.append(BigExp(*map(int, line.strip().split(','))))
    print max(xrange(len(nums)), key=lambda i: nums[i]) + 1 # 1-indexed

if __name__ == '__main__':
    main()

# A googol (10^(100)) is a massive number: one followed by one-hundred zeros; 
# 100^(100) is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a^(b), where a, b < 100, what is 
# the maximum digital sum?

from operator import itemgetter

def digital_sum(number):
    return sum([ int(digit) for digit in str(number) ])

def find_largest_digital_sum(limit):
    return max([ ((a,b), digital_sum(a**b)) for a in xrange(2,limit)
                                            for b in xrange(2,limit) ],
               key = itemgetter(1))

if __name__ == "__main__":
    print 'Largest Digital Sum: %s: %d' % find_largest_digital_sum(100)

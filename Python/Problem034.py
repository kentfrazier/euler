# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of 
# their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def digit_factorial_sum(num):
    return sum([ factorial(int(digit)) for digit in str(num) ])

def _max_num_len():
    test_num = 0
    
    while True:
        test_num = 10 * test_num + 9

        test_len = len(str(test_num))
        fact_len = len(str(digit_factorial_sum(test_num)))

        if test_len > fact_len:
            return fact_len

def combinations(seq, len_min, len_limit, repetition=False, order_important=False):

    if len_limit <= 0:
        yield tuple()
        raise StopIteration()

    max_diff = max(0, len_limit - len_min)

    for diff in xrange(max_diff,-1,-1):

        for i in xrange(len(seq)):

            if repetition:
                if order_important:
                    rest = combinations(seq, len_min, len_limit - (diff + 1), True, True)
                else:
                    rest = combinations(seq[i:], len_min, len_limit - (diff + 1), True)
            else:
                new_seq = seq[0:i] + seq[i+1:]
                rest = combinations(new_seq, len_min, len_limit - (diff + 1))

            for tail in rest:
                yield ( seq[i], ) + tail

def fact_sum_numbers():
    limit = _max_num_len()
    digit_factorials = [ factorial(n) for n in range(10) ]
    seqs = combinations(digit_factorials,2,limit,repetition=True)
    sums = set([ sum(seq) for seq in seqs ])

    return [ n for n in sums if len(str(n)) > 1 and n == digit_factorial_sum(n) ]

if __name__ == "__main__":
    assert( digit_factorial_sum(145) == 145 )

    print sum(fact_sum_numbers())

# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from p012 import factors

def proper_divisors(num):
    return factors(num)[:-1]

sum_of_factors_cache = {}
def sum_of_factors(num):
    global sum_of_factors_cache

    sof = sum_of_factors_cache.get(num)
    if not sof:
        sof = sum(proper_divisors(num))
        sum_of_factors_cache[num] = sof
    return sof

def is_amicable(num):
    sof = sum_of_factors(num)

    if sof == num: return False

    if sum_of_factors(sof) == num:
        return True
    else:
        return False

def amicable_numbers(limit):
    for n in xrange(1,limit):
        if is_amicable(n):
            yield n

def sum_of_amicable_numbers(limit):
    return sum(amicable_numbers(limit))

if __name__ == "__main__":
    print sum_of_amicable_numbers(10000)

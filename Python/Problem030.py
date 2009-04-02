# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:
# 
#     1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
#     8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
#     9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)
# 
# As 1 = 1^(4) is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

def power_sum(power):
    def p_sum(number):
        return sum([ int(digit)**power for digit in str(number) ])
    return p_sum

def power_sum_match_list(power):
    power_sum_fn = power_sum(power)

    test_num = 0
    while True:
        test_num = (test_num * 10) + 9
        if len(str(test_num)) == len(str(power_sum_fn(test_num))):
            len_limit = len(str(test_num))
            break

    matches = []
    for num in xrange(10,10**len_limit):
        if num == power_sum_fn(num):
            matches.append(num)

    return matches

if __name__ == "__main__":
    assert(sum(power_sum_match_list(4)) == 19316)
    print sum(power_sum_match_list(5))

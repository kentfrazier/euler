# The 5-digit number, 16807=7^(5), is also a fifth power. Similarly, the 
# 9-digit number, 134217728=8^(9), is a ninth power.
# 
# How many n-digit positive integers exist which are also an nth power?

from itertools import takewhile, count

def n_digit_n_power_nums():
    limit = len(list(takewhile(lambda x: (x - len(str(9**x))) == 0, count(1))))

    for n in xrange(1,limit+1):
        for i in xrange(1,10):
            power = i**n
            if len(str(power)) == n:
                yield power

if __name__ == "__main__":
    print len(list(n_digit_n_power_nums()))

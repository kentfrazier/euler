# A number chain is created by continuously adding the square of the digits 
# in a number to form a new number until it has been seen before.
# 
# For example,
# 
# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# 
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
# loop. What is most amazing is that EVERY starting number will eventually 
# arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

from itertools import imap

transforms = {}

def transform(n):
    global transforms

    try:
        return transforms[n]
    except KeyError:
        transforms[n] = sum( int(digit)**2 for digit in str(n) )
        return transforms[n]

def number_chain(fn, start, terminate):
    num = start
    while True:
        yield num

        if terminate(num):
            break

        num = fn(num)

def analyze():
    def end(n):
        return n == 1 or n == 89

    return sum(imap(lambda seq: list(seq)[-1] == 89,
            ( number_chain(transform, n, end) for n in xrange(1,10000000) )))

if __name__ == "__main__":
    print analyze()

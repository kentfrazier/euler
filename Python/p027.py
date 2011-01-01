# Euler published the remarkable quadratic formula:

# n^(2) + n + 41

# It turns out that the formula will produce 40 primes for the consecutive 
# values n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 
# 41 is divisible by 41, and certainly when n = 41, 41^(2) + 41 + 41 is clearly 
# divisible by 41.

# Using computers, the incredible formula  n^(2) - 79n + 1601 was discovered, 
# which produces 80 primes for the consecutive values n = 0 to 79. The 
# product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:

#     n^(2) + an + b, where |a| < 1000 and |b| < 1000

#     where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.

from p010 import prime_list3

primes = set(prime_list3(79**2 + 999*79 + 1000))

def quadratic_fn(a,b):
    def fn(n):
        return n**2 + (a * n) + b
    return fn

class Quadratic(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.fn = quadratic_fn(a,b)

    def primes(self):
        i = 0
        while True:
            if self.fn(i) not in primes:
                return i
            i += 1

    def __str__(self):
        return 'n^2 + %dn + %d' % (self.a, self.b)

def quadratics(min_a, max_a, min_b, max_b):
    for a in xrange(min_a,max_a+1):
        for b in xrange(min_b,max_b+1):
            if b not in primes: continue
            yield Quadratic(a,b)

def find_best_prime_quad(min_a, max_a, min_b, max_b):
    best_quad = None
    best_num_primes = 0

    for quad in quadratics(min_a, max_a, min_b, max_b):
        if quad.fn(best_num_primes) not in primes:
            continue
        quad_num_primes = quad.primes()
        if quad_num_primes > best_num_primes:
            best_num_primes = quad_num_primes
            best_quad = quad

    return best_quad

if __name__ == "__main__":
    best = find_best_prime_quad(-999,999,-999,999)

    print best
    print 'Number of Primes:', best.primes()
    print 'a * b =', best.a * best.b

# We shall say that an n-digit number is pandigital if it makes use of all 
# the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 
# 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only 
# include it once in your sum.

from itertools import permutations, chain
from functools import reduce

def pandigital_numbers(minimum=0,limit=None):
    for length in range(1,10):
        for perm in permutations(range(1,length+1)):
            yield reduce(lambda x, y: 10*x + y, perm)

def render_to_number(seq):
    return reduce(lambda x, y: 10*x + y, seq)

def pandigital_products():
    start_set = set(range(1,10))

    def complete_pandigital(product, a, remaining):
        product = render_to_number(product)
        a = render_to_number(a)
        b, remainder = divmod(product, a)
        if remainder: return None
        b = tuple([ int(digit) for digit in str(b) ])
        if set(b) == remaining:
            return b

    for product in permutations(start_set,4):
        remaining = start_set - set(product)

        for a in chain(permutations(remaining,4),permutations(remaining,3)):
            b =  complete_pandigital(product, a, remaining - set(a))
            if b:
                yield tuple(map(render_to_number, (a, b, product)))

if __name__ == "__main__":
    pan_products = list(pandigital_products())
    from pprint import pprint
    pprint(pan_products)
    print sum(set([ seq[2] for seq in pan_products ]))

# By replacing the 1st digit of *3, it turns out that six of the 
# nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# 
# By replacing the 3rd and 4th digits of 56**3 with the same 
# digit, this 5-digit number is the first example having seven primes 
# among the ten generated numbers, yielding the family: 56003, 56113, 
# 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being 
# the first member of this family, is the smallest prime with this 
# property.
# 
# Find the smallest prime which, by replacing part of the number (not 
# necessarily adjacent digits) with the same digit, is part of an 
# eight prime value family.

from p049 import is_prime
from itertools import product, count

def f(n):
    if n == 2:
        return 4
    return ((10 * (n-1)) + 1) * f(n-1) 

def template_gen(num_digits):
    last = ['1','3','7','9']
    middle = [ str(i) for i in range(10) ] + ['*']
    first = [ str(i) for i in range(1,10) ] + ['*']
    product_args = [first] + [middle for i in range(num_digits-2)] + [last]
    for template in product(*product_args):
        if '*' in template:
            yield ''.join(template)

def yield_template_primes(template):
    for num in [ str(i) for i in range(10) ]:
        potential = int(template.replace('*', num))
        if is_prime(potential):
            yield potential

def find_max_template_primes(num_digits):
    def prime_list_length(template):
        return len(list(yield_template_primes(template)))
    return max(( template for template in template_gen(num_digits) ), key=prime_list_length)

def find_first_to_n_primes(n):
    for i in count(2):
        for template in template_gen(i):
            if len(list(yield_template_primes(template))) >= n:
                return template

if __name__ == "__main__":
    print yield_template_primes(find_first_to_n_primes(8)).next()

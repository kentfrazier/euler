# The primes 3, 7, 109, and 673, are quite remarkable. By taking any 
# two primes and concatenating them in any order the result will 
# always be prime. For example, taking 7 and 109, both 7109 and 1097 
# are prime. The sum of these four primes, 792, represents the lowest 
# sum for a set of four primes with this property.
# 
# Find the lowest sum for a set of five primes for which any two 
# primes concatenate to produce another prime.

from itertools import dropwhile, permutations
from collections import defaultdict
from math import floor, log10

from Problem010 import prime_sieve
from Problem049 import is_prime

primes = prime_sieve(10000)
primes.remove(2) # Can never be in a set of more than one
primes.remove(5) # Can never be in a set of more than one

blacklist = {}
good_sets = defaultdict(list)

def is_concatenable_pair(x, y):
    pair = (x, y)
    if blacklist.get(pair):
        return False
    for n, m in permutations(pair, 2):
        if not is_prime(int(m + n * 10**(floor(log10(m)+1)))):
            blacklist[pair] = True
            return False
    return True

def concatenable_prime_set(size, maximum=None):

    if size == 1:
        for prime in primes:
            if maximum is not None and prime >= maximum:
                return
            yield (prime,)
        return

    if len(good_sets[size]) > 0:
        for good_set in good_sets[size]:
            yield good_set
        min_limit = good_sets[size][-1][-1] + 1
    else:
        min_limit = concatenable_prime_set(size - 1).next()[-1] + 1

    for largest in dropwhile(lambda x: x < min_limit, primes):
        if maximum is not None and largest >= maximum:
            return

        for test_set in concatenable_prime_set(size - 1, largest):
            valid = True
            for test_num in test_set:
                if not is_concatenable_pair(test_num, largest):
                    valid = False
                    break
            if not valid:
                continue

            successful_set = test_set + (largest,)
            good_sets[size].append(successful_set)
            yield successful_set

if __name__ == "__main__":
    assert(sum(concatenable_prime_set(4).next()) == sum([3, 7, 109, 673]))
    prime_set = concatenable_prime_set(5).next()
    print prime_set
    print sum(prime_set)

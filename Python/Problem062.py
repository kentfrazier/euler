# The cube, 41063625 (345^(3)), can be permuted to produce two other 
# cubes: 56623104 (384^(3)) and 66430125 (405^(3)). In fact, 41063625 
# is the smallest cube which has exactly three permutations of its 
# digits which are also cube.
# 
# Find the smallest cube for which exactly five permutations of its 
# digits are cube.

from math import log10
from itertools import permutations, ifilter, count

import psyco
psyco.full()

#from Problem032 import render_to_number

def render_to_number(seq):
    return int(''.join(seq))

def split_to_digits(number):
    return [ number // 10**power % 10 for power in xrange(int(log10(number)), -1, -1) ]

split_to_digits = str

def cube_root(number):
    return pow(number, 1./3.)

def is_perfect_cube(number):
    return pow(round(cube_root(number)), 3) == number

def cube_permutations(perm_count):
    for number in ( i ** 3 for i in count(1) ):
        digits = split_to_digits(number)
        
        cubes = []
        for cube in ifilter(is_perfect_cube, ( render_to_number(seq) for seq in set(permutations(digits)) if seq[0] != '0' )):
            cubes.append(cube)
        if len(cubes) >= perm_count:
            print sorted(cubes)
            return sorted(cubes)

if __name__ == "__main__":
    assert( cube_permutations(3)[0] == 41063625 )

    #seq = cube_permutations(5)
    #print 'Cubes:', seq
    #print 'Smallest:', seq[0]

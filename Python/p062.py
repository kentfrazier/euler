"""
The cube, 41063625 (345^(3)), can be permuted to produce two other 
cubes: 56623104 (384^(3)) and 66430125 (405^(3)). In fact, 41063625 
is the smallest cube which has exactly three permutations of its 
digits which are also cube.

Find the smallest cube for which exactly five permutations of its 
digits are cube.
"""

import itertools
import collections

def cube_permutations(number):
    cubes = collections.defaultdict(list)
    for cube in ( i ** 3 for i in itertools.count(2)):
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for digit in (int(char) for char in str(cube)):
            digits[digit] += 1
        digit_tuple = tuple(digits)
        cubes[digit_tuple].append(cube)

        perms = cubes[digit_tuple]
        if len(perms) == number:
            return perms

def main():
    assert(cube_permutations(3)[0] == 41063625)
    print cube_permutations(5)[0]

if __name__ == '__main__':
    main()

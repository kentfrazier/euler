# The cube, 41063625 (345^(3)), can be permuted to produce two other 
# cubes: 56623104 (384^(3)) and 66430125 (405^(3)). In fact, 41063625 
# is the smallest cube which has exactly three permutations of its 
# digits which are also cube.
# 
# Find the smallest cube for which exactly five permutations of its 
# digits are cube.

from math import log10
from itertools import permutations, ifilter, count
from collections import defaultdict

def _append_num(x, y):
    return 10 * x + y

def render_to_number2(seq):
    return reduce(_append_num, seq)

def split_to_digits2(number):
    return [ number // 10**power % 10 for power in xrange(int(log10(number)), -1, -1) ]

split_to_digits = str
render_to_number = int

def cube_root(number):
    return pow(number, 1./3.)

def is_perfect_cube(number):
    return abs(1 - cube_root(number) % 1) < 0.0000001

def cube_permutations(perm_count):
    def digit_permutations(digits):
        for perm in set(permutations(digits)):
            yield ''.join(perm)

    already_processed = set()

    min_cube_root = int(cube_root(int(''.join( str(i) for i in range(1, perm_count + 1) )))) + 1

    for number in ( i ** 3 for i in count(min_cube_root) ):
        number_str = str(number)
        test_str = ''.join(sorted(number_str))
        if test_str in already_processed:
            continue

        already_processed.add(test_str)

        cubes = list( cube for cube in ifilter(is_perfect_cube, ( render_to_number(seq) for seq in digit_permutations(number_str) if seq >= number_str )) )

        if len(cubes) >= perm_count:
            print sorted(cubes)
            return sorted(cubes)

def cube_permutations2(perm_count):
    def number_permutations(digits):
        for perm in set(permutations(digits)):
            yield int(''.join(perm))

    min_cube_root = int(cube_root(int(''.join( str(i) for i in range(1, perm_count + 1) )))) + 1

    perm_cubes = defaultdict(int)

    for signature in ( ''.join(sorted(str(i ** 3))) for i in count(min_cube_root) ):
        perm_cubes[signature] += 1
        if perm_cubes[signature] >= perm_count:
            return list(sorted( cube for cube in number_permutations(signature) if is_perfect_cube(cube) ))
        
class UniqueDigitSetNumber(long):
    _hash_values = dict( (str(i), 2 ** (i * 4)) for i in xrange(10) )

    def __new__(cls, value=0):
        number = super(UniqueDigitSetNumber, cls).__new__(cls, value) # Why must cls be passed to super and to the result?
        number._hash = cls._generate_hash(number)
        return number

    @classmethod
    def _generate_hash(cls, number):
        return sum( cls._hash_values[digit] for digit in split_to_digits(number) )
    @classmethod
    def render_digits_from_hash(cls, hash):
        digits = []
        for key, value in sorted(cls._hash_values.iteritems(), reverse=True):
            count, hash = divmod(hash, value)
            digits += [key] * count
        return digits
    @classmethod
    def create_instance_from_hash(cls, hash):
        return cls(render_to_number2(cls.render_digits_from_hash(hash)))

    def __eq__(self, other):
        return self._hash == other._hash
    def __hash__(self):
        return self._hash

    def render_digits(self):
        return UniqueDigitSetNumber.render_digits_from_hash(self._hash)
    def permutations(self):
        for seq in sorted(set(permutations(self.render_digits()))):
            if seq[0] == '0': continue
            yield render_to_number(''.join(seq))

def cube_permutations3(perm_count):
    min_cube_root = int(cube_root(int(''.join( str(i) for i in range(1, perm_count + 1) )))) + 1

    perm_cubes = defaultdict(int)

    #for number in ( UniqueDigitSetNumber(i ** 3) for i in count(min_cube_root) ):
    for cnt, number in enumerate(( UniqueDigitSetNumber(i ** 3) for i in count(123456789) )):
        print cnt, int(cube_root(number)) # not moving past 8184?  Weird
        num_hash = number.__hash__() # not sure why, but hash(number) returns a different value than this
        perm_cubes[num_hash] += 1
        if perm_cubes[num_hash] >= perm_count:
            return list(filter(is_perfect_cube, number.permutations()))


if __name__ == "__main__":
    assert( cube_permutations3(3)[0] == 41063625 )

    seq = cube_permutations3(5)
    print 'Cubes:', seq
    print 'Smallest:', seq[0]

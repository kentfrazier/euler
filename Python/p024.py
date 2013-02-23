# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of the
# permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#                  012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def lex_permutations(digits):
    digits = set(digits)

    if len(digits) == 1:
        yield list(digits)
        raise StopIteration()

    for digit in sorted(digits):
        remaining_digits = digits.copy()
        remaining_digits.remove(digit)

        for perm in lex_permutations(remaining_digits):
            yield [digit] + perm

def nth_lex_permutation(digits,n):
    permutations = lex_permutations(digits)

    for i in range(n):
        perm = permutations.next()

    return perm

if __name__ == "__main__":
    print ''.join([ str(n) for n in nth_lex_permutation([0,1,2,3,4,5,6,7,8,9], 1000000) ])

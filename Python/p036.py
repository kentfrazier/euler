# The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both 
# bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic 
# in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include 
# leading zeros.)

from __future__ import division
import math

def is_palindrome(string):
    seg_length = int(math.ceil( len(string) / 2 ))

    if string[:seg_length] == ''.join(reversed(string[-seg_length:])):
        return True

    return False

def is_palindrome_in_bases_10_and_2(number):
    return is_palindrome(str(number)) and is_palindrome(bin(number)[2:])

if __name__ == "__main__":
    assert(is_palindrome_in_bases_10_and_2(585))

    print sum([ num for num in xrange(1000000) if is_palindrome_in_bases_10_and_2(num) ])

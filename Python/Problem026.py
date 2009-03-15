# A unit fraction contains 1 in the numerator. The decimal 
# representation of the unit fractions with denominators 2 to 10 are 
# given:
#
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It 
# can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest 
# recurring cycle in its decimal fraction part.

from __future__ import division

class NotRepeating(Exception):
    pass

def repeating_seq(divisor):
    sequences = {}

    numerator = 1

    while True:
        if numerator == 0:
            raise NotRepeating('Decimal does not repeat.')

        numerator = 10 * remainder

        digit, remainder = divmod(numerator, divisor)
        # TODO: figure out how to store these results and check them

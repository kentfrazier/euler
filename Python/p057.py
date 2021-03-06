# It is possible to show that the square root of two can be expressed 
# as an infinite continued fraction.
# 
# sqrt 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# 
# By expanding this for the first four iterations, we get:
# 
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# 
# The next three expansions are 99/70, 239/169, and 577/408, but the 
# eighth expansion, 1393/985, is the first example where the number 
# of digits in the numerator exceeds the number of digits in the 
# denominator.
# 
# In the first one-thousand expansions, how many fractions contain a 
# numerator with more digits than denominator?

from fractions import Fraction

def continued_fraction_gen():
    current = Fraction(1,1)
    yield current

    while True:
        new_denominator = current.numerator + current.denominator
        new_numerator = new_denominator + current.denominator
        current = Fraction(new_numerator, new_denominator)
        yield current

if __name__ == "__main__":
    from itertools import islice

    print len([ frac for frac in islice(continued_fraction_gen(), 1000) if len(str(frac.numerator)) > len(str(frac.denominator)) ])

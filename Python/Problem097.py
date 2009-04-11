# The first known prime found to exceed one million digits was discovered in 
# 1999, and is a Mersenne prime of the form 2^(6972593)-1; it contains 
# exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 
# 2^(p)-1, have been found which contain more digits.
# 
# However, in 2004 there was found a massive non-Mersenne prime which 
# contains 2,357,207 digits: 28433*2^(7830457)+1.
# 
# Find the last ten digits of this prime number.

def pow_mod(base, expt, mod):
    def iter(base, expt, multiplier):
        base %= mod
        multiplier %= mod

        if expt == 1:
            return (multiplier * base) % mod 

        if expt & 1 == 1:
            return iter(base, expt - 1, multiplier * base)

        return iter(base**2, expt // 2, multiplier)

    return iter(base, expt, 1)

if __name__ == "__main__":
    print ( 28433 * pow_mod(2,7830457,10**10) + 1 ) % 10**10

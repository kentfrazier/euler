# Triangle, pentagonal, and hexagonal numbers are generated by the following 
# formulae:
#
# Triangle      T_(n)=n(n+1)/2     1, 3, 6, 10, 15, ...
# Pentagonal    P_(n)=n(3n-1)/2    1, 5, 12, 22, 35, ...
# Hexagonal     H_(n)=n(2n-1)      1, 6, 15, 28, 45, ...
# 
# It can be verified that T_(285) = P_(165) = H_(143) = 40755.
# 
# Find the next triangle number that is also pentagonal and hexagonal.

from Problem042 import triangle

def pentagonal(n):
    return (n * (3*n - 1)) / 2

def hexagonal(n):
    return n * (2*n - 1)

def fn_num_gen(fn, min=0, limit=None, step=1):
    n = min
    while limit is None or n < limit:
        yield fn(n)
        n += step

if __name__ == "__main__":
    triangles = fn_num_gen(triangle, 285 + 1)
    pentagonals = set(fn_num_gen(pentagonal, 165 + 1, 100000))
    hexagonals = set(fn_num_gen(hexagonal, 143 + 1, 100000))

    pent_hex = pentagonals & hexagonals

    for tri in triangles:
        if tri in pent_hex:
            print tri
            break

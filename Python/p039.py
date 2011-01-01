# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p <= 1000, is the number of solutions maximised?

from collections import defaultdict
from math import hypot

def find_integral_triangles(max_perimeter):
    integral_triangles = defaultdict(list)

    for a in xrange(1, max_perimeter // 3):
        for b in xrange(a, (max_perimeter - a) // 2):
            c = hypot(a,b)

            if a+b+c > max_perimeter: continue

            if c % 1 == 0:
                integral_triangles[int(a+b+c)].append((a,b,int(c)))

    return integral_triangles

def max_len_key(map):
    def cmp_fn(key):
        return len(map[key])

    return max(map, key=cmp_fn)

if __name__ == "__main__":
    integrals = find_integral_triangles(1000)

    assert( integrals[120] == [(20,48,52),(24,45,51),(30,40,50)] )

    max_num = max_len_key(integrals)

    from pprint import pprint

    print 'Max number:', max_num
    pprint(integrals[max_num])

"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
each line adding to nine.

Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set: 4,3,2;
6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total.

Total	Solution Set
9	    4,2,3; 5,3,1; 6,1,2
9	    4,3,2; 6,2,1; 5,1,3
10      2,3,5; 4,5,1; 6,1,3
10      2,5,3; 6,3,1; 4,1,5
11      1,4,6; 3,6,2; 5,2,4
11      1,6,4; 5,4,2; 3,2,6
12      1,5,6; 2,6,4; 3,4,5
12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to
form 16- and 17-digit strings. What is the maximum 16-digit string for a
"magic" 5-gon ring?
"""

from itertools import permutations

def magic_ring_gen(sides):
    def key_fn(chain):
        return chain[1][0]

    outer_nodes = range(sides, 2 * sides)
    paths = [(node, node - sides, (node - sides + 1) % sides)
             for node in outer_nodes]

    numbers = range(1, 2 * sides + 1)
    for nodes in permutations(numbers):
        chains = [(path, tuple(nodes[i] for i in path)) for path in paths]
        totals = set(sum(chain[1]) for chain in chains)
        if len(totals) == 1:
            index = min(chains, key=key_fn)[0][0]
            yield tuple(chains[(index + i) % sides][1] for i in xrange(sides))

def max_solution_num(sides):
    max_solution = max(magic_ring_gen(sides))

    return int(
        ''.join(
            ''.join(str(n) for n in group)
            for group in max_solution
        )
    )

def main():
    assert(max_solution_num(3) ==  432621513)
    print max_solution_num(5)

if __name__ == "__main__":
    main()

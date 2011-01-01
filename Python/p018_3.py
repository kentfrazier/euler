# By starting at the top of the triangle below and moving to adjacent 
# numbers on the row below, the maximum total from top to bottom is 23.
#
# (see triangle_text_small below)
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
# 
# (see triangle_text_large below)

from __future__ import division
from math import ceil

class Row(list):
    def elements(self):
        for element in self:
            yield element

    def __str__(self):
        return '  '.join([ '%02d' % item for item in self ])

class Triangle(list):
    def __init__(self, rows):
        row_list = [ Row(row) for row in rows ]
        super(Triangle, self).__init__(row_list)

    def pretty_print(self):
        max_length = len(str(self[-1]))

        for row in self:
            print ' ' * ( (max_length - len(str(row))) // 2 ) + str(row)

    def largest_seq_sum(self):
        clone = [ row[:] for row in self[:] ]
        for i in range(len(clone)-1,0,-1):
            for j in range(len(clone[i-1])):
                clone[i-1][j] += max(clone[i][j], clone[i][j+1])

        return clone[0][0]


def parse_triangle(triangle_text):
    rows = [ row for row in triangle_text.strip('\n').split('\n') ]

    parsed_rows = []

    for row_text in rows:
        items = [ int(num.lstrip('0')) for num in row_text.strip().split() ]
        parsed_rows.append(items)
    
    return parsed_rows


triangle_text_small = """
3
7 5
2 4 6
8 5 9 3
"""

triangle_text_large = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

if __name__ == "__main__":
    triangle = Triangle(parse_triangle(triangle_text_large))
    print triangle.largest_seq_sum()

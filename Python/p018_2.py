from __future__ import division
from math import ceil

class Row(tuple):
    def elements(self):
        for element in self:
            yield element

    def left_sum(self):
        return sum([ num for num in self[:int(ceil(len(self)/2))] ])

    def right_sum(self):
        return sum([ num for num in self[(len(self)//2):] ])

    def average(self):
        return sum(self) / len(self)

    def __str__(self):
        return '  '.join([ '%02d' % item for item in self ])

class Triangle(list):
    def __init__(self, rows):
        self.row_list = [ Row(row) for row in rows ]
        super(Triangle, self).__init__(self.row_list)

    def rows(self):
        for row in self:
            yield row

    def triangle_sum(self):
        return sum([ sum(row) for row in self ])

    def element_count(self):
        return sum([ len(row) for row in self ])

    def left_side_sum(self):
        return sum([ row.left_sum()  for row in self ])

    def right_side_sum(self):
        return sum([ row.right_sum() for row in self ])

    def average(self):
        return self.triangle_sum() / self.element_count()

    def larger_child(self):
        """
        Of the two triangles starting on the next row, should return
        the larger one.  This doesn't work properly.
        """

        left_child = self.left_child_triangle()
        right_child = self.right_child_triangle()

        left_avg = left_child.average()
        right_avg = right_child.average()
        avg_diff = left_avg - right_avg
        el_diff = left_child[0][0] - right_child[0][0]
        compound_diff = avg_diff + el_diff

        if compound_diff > 0:
            return left_child
        else:
            return right_child

    def left_child_triangle(self):
        return Triangle([ row[:-1] for row in self[1:] ])

    def right_child_triangle(self):
        return Triangle([ row[1:] for row in self[1:] ])

    def largest_sequence(self):
        if len(self) == 1:
            return self[0]

        return self[0] + self.larger_child().largest_sequence()

    def pretty_print(self):
        max_length = len(str(self[-1]))

        for row in self:
            print ' ' * ( (max_length - len(str(row))) // 2 ) + str(row)

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

triangle_text_small2 = """
3
7 5
4 2 6
8 5 20 9
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

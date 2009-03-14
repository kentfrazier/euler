class Element(object):
    def __init__(self,value,list_pos,row):
        self.value = value
        self.row = row
        self.position = 2 * (list_pos - (row.length // 2))
        if row.length % 2 == 0:
            self.position += 1

    def adjacent_to(self, element):
        if element == None: return False

        if abs(self.row.position - element.row.position) <= 1 and \
                abs(self.position - element.position) <= 1:
            return True
        else:
            return False

    def __unicode__(self):
        return str(self.value)


class Row(list):
    def __init__(self, row_text, position, triangle):
        self.triangle = triangle
        self.position = position

        items = [ int(num.lstrip('0')) for num in row_text.strip().split() ]
        self.length = len(items)

        self.elements = {}
        for i in range(len(items)):
            element = Element(items[i], i, self)
            self.append(element)
            self.elements[element.position] = element

    def __unicode__(self):
        return '  '.join([ '%02d' % item.value for item in self ])

    def sequences(self, calling_el=None):
        if self == self.triangle.rows[-1]: # last row
            for el in self:
                if calling_el == None or el.adjacent_to(calling_el):
                    yield [el] 
        else:
            for el in self:
                if calling_el == None or el.adjacent_to(calling_el):
                    for seq in self.triangle.rows[self.position+1].sequences(el):
                        yield [el] + seq
        
class Triangle(object):
    def __init__(self, triangle_text):
        rows = [ row for row in triangle_text.strip('\n').split('\n') ]

        self.rows = []
        for i in range(len(rows)):
            self.rows.append(Row(rows[i], i, self))

    def pretty_print(self):
        max_length = len(str(self.rows[-1]))

        for row in self.rows:
            print ' ' * ( (max_length - len(str(row))) // 2 ) + str(row)

    def sequences(self):
        for seq in self.rows[0].sequences():
            yield [ el.value for el in seq ]

    def brute_force_largest_sequence(self):
        largest_sum = 0

        for seq in self.sequences():
            seq_sum = sum(seq)
            if seq_sum > largest_sum:
                largest_seq = seq
                largest_sum = seq_sum

        return largest_seq



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

if __name__ == "__main__":
    triangle = Triangle(triangle_text_large)

    largest_seq = triangle.brute_force_largest_sequence()

    print largest_seq
    print 'Sum:', sum(largest_seq)

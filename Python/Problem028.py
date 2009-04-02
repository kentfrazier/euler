# Starting with the number 1 and moving to the right in a clockwise direction 
# a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of both diagonals is 101.
# 
# What is the sum of both diagonals in a 1001 by 1001 spiral formed in the 
# same way?

from __future__ import division
import math

class Spiral(dict):
    def __init__(self, size, start_number=1):
        if size < 1:
            raise Exception('Size parameter too small')

        self.width = 1
        self.height = 1

        x = y = 0

        current = start_number 
        self[(x,y)] = current
        run_length = 1

        def change_direction():
            while True:
                yield (1,0)
                yield (0,-1)
                yield (-1,0)
                yield (0,1)

        direction = change_direction()

        while self.width <= size or self.height < size:

            x_step, y_step = direction.next()

            if x_step:
                self.width += 1
            else:
                self.height += 1

            for i in xrange(run_length):
                x += x_step
                y += y_step
                current += 1

                self[(x,y)] = current

            if self.width > run_length and self.height > run_length and run_length < size-1:
                run_length += 1

    def sum_diagonals(self):
        return sum([ self[key] for key in self.keys() if abs(key[0]) == abs(key[1]) ])

    def __str__(self):
        keys = self.keys()
        x_list = [key[0] for key in keys]
        min_x = min(x_list)
        max_x = max(x_list)
        y_list = [key[1] for key in keys]
        min_y = min(y_list)
        max_y = max(y_list)

        rows = []

        for y in xrange(max_y,min_y-1,-1):
            row = []
            for x in xrange(min_x,max_x+1):
                row.append(self.get((x,y),0))
            rows.append(row)

        return '\n'.join([' '.join(['%4d' % el for el in row]) for row in rows])

if __name__ == "__main__":
    assert(Spiral(5).sum_diagonals() == 101)
    print Spiral(1001).sum_diagonals()

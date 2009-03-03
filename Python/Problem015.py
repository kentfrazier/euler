# Starting in the top left corner of a 2x2 grid, there are 6 
# routes (without backtracking) to the bottom right corner.
# 
# How many routes are there through a 20x20 grid?

def Point(object):
    pass

def Grid(dict):
    def __init__(self,height,width):
        super(Grid,self).__init__()

        self.height = height
        self.width = width

        for y in range(height+1):
            for x in range(width+1):
                self[(x, y)] = Point(self, x, y)

    def generate_paths(self, start, end):
        if start.x < self.width:
            yield [start] + self.generate_paths((start.x+1, start.y), end)

        if start.y < self.height:
            yield [start] + self.generate_paths((start.x, start.y+1), end)

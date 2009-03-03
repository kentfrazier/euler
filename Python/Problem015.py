# Starting in the top left corner of a 2x2 grid, there are 6 
# routes (without backtracking) to the bottom right corner.
# 
# How many routes are there through a 20x20 grid?

def find_paths(start, end):

    x_change = 1 if start[0] < end[0] else -1
    y_change = 1 if start[1] < end[1] else -1

    if start[0] != end[0]:
        for path in find_paths((start[0] + x_change, start[1]), end):
            yield [start] + path

    if start[1] != end[1]:
        for path in find_paths((start[0], start[1] + y_change), end):
            yield [start] + path

    if start == end:
        yield [end]

path_counts = {}

def count_paths(start, end):

    if start[0] == end[0] or start[1] == end[1]:
        return 1

    x_change = 1 if start[0] < end[0] else -1
    new_x = (start[0] + x_change, start[1])

    y_change = 1 if start[1] < end[1] else -1
    new_y = (start[0], start[1] + y_change)

    global path_counts

    paths = path_counts.get((start,end))

    if not paths:
        paths = count_paths(new_x, end) + count_paths(new_y, end)
        path_counts[(start,end)] = paths

    return paths

if __name__ == "__main__":
    print count_paths((0,0),(20,20))

"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427. (actually brackets)

[131]  673   234   103   18
[201] [96 ] [342]  965   150
 630   803  [746] [422]  111
 537   699   497  [121]  956
 805   732   524  [37 ] [331]

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the
bottom right by only moving right and down.
"""

from copy import deepcopy

def convert_matrix_string(matrix_str):
    return [map(int, line.strip().split(','))
            for line in matrix_str.strip().split('\n')]

def minimal_path_sum(matrix):
    matrix = deepcopy(matrix)
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1
    for x in xrange(max_x - 1, -1, -1):
        matrix[x][max_y] += matrix[x + 1][max_y]
    for y in xrange(max_y - 1, -1, -1):
        matrix[max_x][y] += matrix[max_x][y + 1]
    for x in xrange(max_x - 1, -1, -1):
        for y in xrange(max_y - 1, -1, -1):
            matrix[x][y] += min(
                matrix[x + 1][y],
                matrix[x][y + 1],
            )
    return matrix[0][0]

def test():
    matrix_str = (
        """
        131,673,234,103,18
        201,96,342,965,150
        630,803,746,422,111
        537,699,497,121,956
        805,732,524,37,331
        """
    )
    matrix = convert_matrix_string(matrix_str)
    min_path = minimal_path_sum(matrix)
    assert(min_path == 2427)

def main():
    test()
    with open('matrix.txt', 'r') as f:
        print minimal_path_sum(convert_matrix_string(f.read().strip()))

if __name__ == '__main__':
    main()

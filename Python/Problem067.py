from Problem018_3 import Triangle, parse_triangle

if __name__ == "__main__":
    f = open('triangle.txt')
    triangle_text = f.read()
    f.close()

    triangle = Triangle(parse_triangle(triangle_text))
    print triangle.largest_seq_sum()

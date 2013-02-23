# It can be seen that the number, 125874, and its double, 251748, contain 
# exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
# contain the same digits.

try:
    import psyco
    psyco.full()
except ImportError:
    pass

def digit_list(number):
    return sorted([ int(digit) for digit in str(number) ])

def test_for_same(number):
    digits = digit_list(number)

    if all( digit_list(number*factor) == digits for factor in range(2,7) ):
        return True

    return False

if __name__ == "__main__":
    num = 1
    while True:
        if test_for_same(num):
            print num
            break

        num += 1

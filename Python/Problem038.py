# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
#     192 * 1 = 192
#     192 * 2 = 384
#     192 * 3 = 576
# 
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We 
# will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
# and 5, giving the pandigital, 918273645, which is the concatenated product 
# of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

from Problem032 import render_to_number

def pandigital_concat_products():
    start_set = set(range(1,10))

    for i in xrange(1,100000):
        remaining = start_set.copy()
        seq = []

        for n in xrange(1,10):
            product = i * n
            product_list = [ int(digit) for digit in str(product) ]
            product_set = set(product_list)

            if len(product_list) != len(product_set):
                break

            if product_set <= remaining:
                remaining -= product_set
                seq += product_list
            else:
                break

            if len(remaining) == 0:
                yield (i, render_to_number(seq))
                break

if __name__ == "__main__":
    print max([ product[1] for product in pandigital_concat_products() ])

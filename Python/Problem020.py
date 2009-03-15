# n! means n x (n - 1) x ... x 3 x 2 x 1
#
# Find the sum of the digits in the number 100!

def factorial(num):
    if num == 1:
        return num
    
    return num * factorial(num - 1)

def sum_of_digits(num):
    return sum([ int(n) for n in str(num) ])

if __name__ == "__main__":
    print sum_of_digits(factorial(100))

# An irrational decimal fraction is created by concatenating the positive 
# integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12^(th) digit of the fractional part is 1.
# 
# If d_(n) represents the n^(th) digit of the fractional part, find the value 
# of the following expression.
# 
# d_(1) x d_(10) x d_(100) x d_(1000) x d_(10000) x d_(100000) x d_(1000000)

def d(pos):
    if pos < 10:
        return pos

    length = 0
    while True:
        length += 1
        period = 9 * length * (10**(length-1))
        if pos > period:
            pos -= period
        else:
            break

    divisor, remainder = divmod(pos, length)

    if remainder == 0:
        return int(str(divisor - 1)[-1])

    result = pos // ( length * 10**(length - remainder) )
    if remainder == 1:
        result += 1

    return int(str(result)[-1])

if __name__ == "__main__":
    import operator
    print reduce(operator.mul, [ d(10**n) for n in range(7) ])

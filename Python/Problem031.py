# In England the currency is made up of pound, P, and pence, p, and there are 
# eight coins in general circulation:
# 
#     1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
# 
# It is possible to make P2 in the following way:
# 
#     1xP1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# 
# How many different ways can P2 be made using any number of coins?

def make_change(amount, coins):
    if amount == 0:
        yield tuple()
        raise StopIteration()

    coins = [ coin for coin in coins if coin <= amount ]

    for i in xrange(len(coins)):
        for tail in make_change(amount - coins[i], coins[i:]):
            yield ( coins[i], ) + tail

if __name__ == "__main__":
    coins = (1, 2, 5, 10, 20, 50, 100, 200)

    ways_to_make_2_pounds = list(make_change(200, coins))

    print len(ways_to_make_2_pounds)

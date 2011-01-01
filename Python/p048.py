# The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.
# 
# Find the last ten digits of the series, 
# 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).

def series_sum(limit):
    return sum([ n**n for n in xrange(1,limit+1) ])

if __name__ == "__main__":
    assert(series_sum(10) == 10405071317)

    print str(series_sum(1000))[-10:]

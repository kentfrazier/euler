# The prime 41, can be written as the sum of six consecutive primes:
#               41 = 2 + 3 + 5 + 7 + 11 + 13
# 
# This is the longest sum of consecutive primes that adds to a prime below 
# one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a 
# prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most 
# consecutive primes?

from p010 import prime_list3 as prime_sieve

def largest_prime_seq(limit):
    primes = prime_sieve(limit)
    prime_set = set(primes)

    # determine the maximum allowable sequence length
    test_num = 0
    for max_seq_len, prime in enumerate(primes):
        test_num += prime
        if test_num > limit: break
        
    for length in xrange(max_seq_len,0,-1):
        for start in xrange(len(primes)-length):
            seq = primes[start:start+length]
            seq_sum = sum(seq)

            if seq_sum >= limit: break

            if seq_sum in prime_set:
                return seq

if __name__ == "__main__":
    assert( sum(largest_prime_seq(100)) == 41 )
    assert( sum(largest_prime_seq(1000)) == 953 )

    million_seq = largest_prime_seq(1000000)

    print 'Largest Sequence:', million_seq
    print 'Number of Primes:', len(million_seq)
    print 'Sum:', sum(million_seq)

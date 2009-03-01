from Problem003 import primes

def get_nth_prime(n):
	prime_generator = primes()

	for i in xrange(n):
		prime = prime_generator.next()
	
	return prime

if __name__ == "__main__":
	print get_nth_prime(10001)

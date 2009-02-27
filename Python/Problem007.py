from Problem3 import next_prime

def get_nth_prime(n):
	prime_generator = next_prime()

	for i in xrange(n):
		prime = prime_generator.next()
	
	return prime

if __name__ == "__main__":
	print get_nth_prime(10001)

import math

def list_primes(limit):
    primes = [2,3]
    num = 3
    while True:
        num += 2
        if num > limit: break
        if any( num % prime == 0 for prime in primes ): continue
        primes.append(num)
    return primes

def next_prime():
    primes = [2,3]
    yield 2
    yield 3
    num = 3
    while True:
        num += 2
        if any( num % prime == 0 for prime in primes ): continue
        primes.append(num)
        yield num

def list_primes2(limit):
    primes = []
    prime_gen = next_prime()

    prime = prime_gen.next()
    while prime < limit:
        primes.append(prime)
        prime = prime_gen.next()

    return primes

def highest_prime_factor(number):
    current = number
    primes = []
    prime_generator = next_prime()

    def get_next_number(num):
        if num in primes: return num

        for p in primes:
            if num % p == 0:
                num /= p
                return get_next_number(num)

        return num

    while current not in primes:
        primes.append(prime_generator.next())
        if primes[-1] > number: return number
        if current == primes[-1]: return current
        if current % primes[-1] == 0:
            current = get_next_number(current/primes[-1])

    return max(primes)

def hpf2(number): # much more efficient algorithm
    
    limit = math.floor(math.sqrt(number))

    divisor = 2

    while divisor < limit and number != divisor:
        if number % divisor == 0:
            number /= divisor
            continue
        divisor += 1 if divisor == 2 else 2
    
    return number

if __name__ == "__main__":
    print highest_prime_factor(600851475143)
    print hpf2(600851475143)

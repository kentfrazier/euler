import math

prime_number_list = [2,3]

def primes(limit=None):
    global prime_number_list

    for prime in prime_number_list:
        if limit and prime > limit: break
        yield prime

    num = prime_number_list[-1]
    while True:
        num += 2

        if limit and num > limit: break

        if any( num % prime == 0 for prime in prime_number_list ): continue

        prime_number_list.append(num)
        yield num

def primes_old(limit):
    prime_list = [2,3]

    yield 2
    yield 3
    num = 3

    while num + 2 < limit:
        num += 2

        if any( num % prime == 0 for prime in prime_list ): continue

        prime_list.append(num)
        yield num

def prime_list(limit):
    return list(primes(limit))

def highest_prime_factor(number):
    
    limit = math.sqrt(number)

    divisor = 2

    while divisor < limit and number != divisor:
        if number % divisor == 0:
            number /= divisor
            continue
        divisor += 1 if divisor == 2 else 2
    
    return number

if __name__ == "__main__":
    print highest_prime_factor(600851475143)

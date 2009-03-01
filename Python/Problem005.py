import math
import Problem003


def list_prime_factors(number):
    current = number
    primes = []
    factors = []
    prime_generator = Problem003.primes(number+1)

    def get_next_number(num):
        if num in primes:
            factors.append(num)
            return num

        for p in primes:
            if num % p == 0:
                factors.append(p)
                num /= p
                return get_next_number(num)

        return num

    while current not in primes:
        try:
            primes.append(prime_generator.next())
        except StopIteration:
            break

        if current % primes[-1] == 0:
            current = get_next_number(current)
    
    assert(number == reduce(lambda x, y: x * y, factors))

    return sorted(factors)

def smallest_multiple(limit):
    if limit < 2:
        raise Exception('Limit passed was too small.')

    factor_dict = {}
    factor_list = []

    for num in range(limit,1,-1):
        factors = list_prime_factors(num)
        for factor in set(factors):
            if factor_dict.get(factor,0) < factors.count(factor):
                factor_dict[factor] = factors.count(factor)

    for factor, count in factor_dict.items():
        factor_list.extend([factor] * count)

    multiple = reduce(lambda x, y: x * y, factor_list)

    assert(all( multiple % n == 0 for n in range(1,limit+1) ))
    return multiple

if __name__ == "__main__":
	print smallest_multiple(20)

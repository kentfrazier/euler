/*
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include <primes.h>

int smallest_divisible_by_range(int);

int smallest_divisible_by_range(int limit) {
    int *prime_counts = malloc(sizeof(int) * (limit + 1)),
        *current_prime_counts = malloc(sizeof(int) * (limit + 1));

    int i,
        j,
        num,
        prime,
        result,
        product = 1;

    PrimeSieve sieve = make_prime_sieve(limit);

    for (i = 2; i <= limit; i++) {
        num = i;
        for (j = 2; j < i; j++) {
            current_prime_counts[j] = 0;
        }
        reset_prime_sieve(&sieve);

        result = next_prime(&sieve, &prime);
        if (result) {
            break;
        }
        while (num > 1) {
            if (num % prime) {
                result = next_prime(&sieve, &prime);
                if (result) {
                    break;
                }
                continue;
            }

            current_prime_counts[prime] += 1;
            num /= prime;
        }

        for (j = 2; j <= limit; j++) {
            if (current_prime_counts[j] > prime_counts[j]) {
                prime_counts[j] = current_prime_counts[j];
            }
        }
    }

    for (i = 2; i <= limit; i += 1) {
        if (prime_counts[i]) {
            product *= pow(i, prime_counts[i]);
        }
    }

    cleanup_prime_sieve(&sieve);
    free(prime_counts);
    free(current_prime_counts);

    return product;
}

int main() {
    printf("%d\n", smallest_divisible_by_range(20));
    return 0;
}

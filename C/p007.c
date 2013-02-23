/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6^(th) prime is 13.

What is the 10001^(st) prime number?
*/

#include <primes.h>

int nth_prime(int);

int nth_prime(int n) {
    PrimeSieve sieve = make_prime_sieve(500000);

    int ret_code, prime;
    for (; n > 0; --n) {
        ret_code = next_prime(&sieve, &prime);
        if (ret_code) {
            cleanup_prime_sieve(&sieve);
            return -1;
        }
    }
    cleanup_prime_sieve(&sieve);
    return prime;
}

int main() {
    printf("%d\n", nth_prime(10001));
    return 0;
}

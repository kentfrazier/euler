#ifndef _PRIMES_H

#define _PRIMES_H 1

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef struct {
    int *numbers;
    int position;
    int limit;
} PrimeSieve;

PrimeSieve make_prime_sieve(int);
void reset_prime_sieve(PrimeSieve *);
void cleanup_prime_sieve(PrimeSieve *);
int next_prime(PrimeSieve *, int *);
int is_prime(int, PrimeSieve *);

PrimeSieve make_prime_sieve(int limit) {
    int *numbers = malloc(sizeof(int) * (limit + 1));

    PrimeSieve sieve = { numbers, 1, limit };

    int i;
    for (i = 2; i <= limit; i++) {
        *(sieve.numbers + i) = 1;
    }

    double limit_sqrt = sqrt((double) limit);

    int num,
        multiple = 0;
    for (num = 2; num <= limit_sqrt; num++) {
        for (i = 2; ; i++) {
            multiple = i * num;
            if (multiple > limit) {
                break;
            }
            *(sieve.numbers + multiple) = 0;
        }
    }

    return sieve;
}

void cleanup_prime_sieve(PrimeSieve *sieve) {
    free(sieve->numbers);
}

void reset_prime_sieve(PrimeSieve *sieve) {
    sieve->position = 1;
}

int is_prime(int num, PrimeSieve *sieve) {
    return *(sieve->numbers + sieve->position);
}

int next_prime(PrimeSieve *sieve, int *prime) {
    do {
        sieve->position += 1;
    } while ((sieve->position <= sieve->limit) &&
            !*(sieve->numbers + sieve->position));

    if (sieve->position > sieve->limit) {
        printf("Exceeded limit: position: %d, limit: %d\n",
               sieve->position, sieve->limit);
        return 1;
    }
    *prime = sieve->position;
    return 0;
}

#endif /* !_PRIMES_H */

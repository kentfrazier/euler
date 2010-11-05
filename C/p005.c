/*
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct prime_sieve make_prime_sieve(int);
void reset_prime_sieve(struct prime_sieve *);
void cleanup_prime_sieve(struct prime_sieve *);
int next_prime(struct prime_sieve *, int *);
int is_prime(int, struct prime_sieve *);
int smallest_divisible_by_range(int);

struct prime_sieve {
    int *numbers;
    int position;
    int limit;
};

struct prime_sieve make_prime_sieve(int limit) {
    int *numbers = malloc(sizeof(int) * (limit + 1));

    struct prime_sieve sieve = { numbers, 1, limit };

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

void cleanup_prime_sieve(struct prime_sieve *sieve) {
    free(sieve->numbers);
}

void reset_prime_sieve(struct prime_sieve *sieve) {
    sieve->position = 1;
}

int is_prime(int num, struct prime_sieve *sieve) {
    return *(sieve->numbers + sieve->position);
}

int next_prime(struct prime_sieve *sieve, int *prime) {
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

int smallest_divisible_by_range(int limit) {
    int *prime_counts = malloc(sizeof(int) * (limit + 1)),
        *current_prime_counts = malloc(sizeof(int) * (limit + 1));

    int i,
        j,
        num,
        prime,
        result,
        product = 1;

    struct prime_sieve sieve = make_prime_sieve(limit);

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
}

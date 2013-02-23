/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>
#include <math.h>

int is_multiple(unsigned long long, unsigned long long);
int is_prime(unsigned long long);
unsigned long long largest_prime_factor(unsigned long long);

int is_multiple(unsigned long long num, unsigned long long divisor) {
    return !(num % divisor);
}

int is_prime(unsigned long long num) {
    if (num == 1) {
        return 0;
    }
    if (num == 2) {
        return 1;
    }
    if (is_multiple(num, 2)) {
        return 0;
    }

    double limit = sqrt((double) num);
    unsigned long long i;

    for (i = 3; i <= limit; i += 2) {
        if (is_multiple(num, i)) {
            return 0;
        }
    }
    return 1;
}

unsigned long long largest_prime_factor(unsigned long long num) {
    unsigned long long limit = num;
    unsigned long long i = 2;

    while (i < num) {
        if (i == num) {
            return i;
        }
        if (is_multiple(num, i)) {
            num /= i;
            continue;
        }

        if (i == 2) {
            i++;
        } else {
            i += 2;
        }
        for (; i < num && !is_prime(i); i += 2)
            ;
    }
}

int main() {
    printf("%llu\n", largest_prime_factor(600851475143LL));
    return 0;
}

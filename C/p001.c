/*
If we list all the natural numbers below 10 that are multiples of 3 
or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/ 

#include <stdio.h>

int is_multiple(int, int);
int sum_of_multiples(int);

int is_multiple(int num, int divisor) {
    return !(num % divisor);
}

int sum_of_multiples(int limit) {
    int sum = 0;
    int i;

    for (i=0; i < limit; i++) {
        if (is_multiple(i, 3) || is_multiple(i, 5)) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    printf("%d\n", sum_of_multiples(1000));
    return 0;
}

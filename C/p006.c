/*
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
*/

#include <stdio.h>
#include <math.h>

int sum_of_squares(int);
int square_of_sum(int);

int sum_of_squares(int limit) {
    int i,
        sum = 0;

    for (i = 1; i <= limit; i++) {
        sum += pow(i, 2);
    }

    return sum;
}

int square_of_sum(int limit) {
    int i,
        sum = 0;

    for (i = 1; i <= limit; i++) {
        sum += i;
    }

    return pow(sum, 2);
}

int main() {
    printf("%d\n", square_of_sum(100) - sum_of_squares(100));

    return 0;
}

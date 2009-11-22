/*
A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 
9009 = 91 × 99.

Find the largest palindrome made from the product of two 
3-digit numbers.
*/

#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAXSIZE 1000

void reverse(char str[]) {
    int i, j;
    char c;

    for (i=0, j=strlen(str)-1; i <= j; i++, j--) {
        c = str[i];
        str[i] = str[j];
        str[j] = c;
    }
}

void itoa(int num, char str[], int radix) {
    int i = 0;
    do {
        str[i++] = num % radix;
        num /= radix;
    } while (num > 0);
    reverse(str);
}

int is_palindrome(char str[]) {
    int i, j;

    for (i=0, j=strlen(str)-1; i <= j; i++, j--) {
        printf("%c, %c", str[i], str[j]);
        if (str[i] != str[j]) {
            return 0;
        }
    }
    return 1;
}

int largest_palindrome(int size) {
    int num1, num2, max, product;
    char str[MAXSIZE];

    max = (int) (pow(10, size) - 1);
    for (num1 = max; num1 >= 0; num1--) {
        for (num2 = max; num2 >= num1; num2--) {
            product = num1 * num2;
            itoa(product, str, 10);
            if (is_palindrome(str)) {
                return product;
            }
        }
    }
}

int main() {
    printf("%d\n", largest_palindrome(2));
    return 0;
}

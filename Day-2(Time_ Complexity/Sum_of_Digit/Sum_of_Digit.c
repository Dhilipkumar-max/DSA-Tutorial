#include<stdio.h>

int sumOfDigits(int n) {
    int sum = 0;
    while (n != 0) {
        int last = n % 10;

        sum += last;

        n /= 10;
    }
    return sum;
}

int main() {
    int n = 12345;
    printf("%d", sumOfDigits(n));
    return 0;
}
// Time Complexity: O(log n) where n is the input number, because we are dividing the number by 10 in each iteration.
// Space Complexity: O(1) because we are using a constant amount of space to store the sum and the last digit.
#include <stdio.h>
void Reverse_Digit(int n) {
    int rev = 0;
    while (n != 0) {
        int last = n % 10;

        rev = rev * 10 + last;

        n /= 10;
    }
    printf("%d", rev);
}
void main() {
    int n = 12345;
    Reverse_Digit(n);
}
// Time Complexity: O(log n) where n is the input number, because we are dividing the number by 10 in each iteration.
// Space Complexity: O(1) because we are using a constant amount of space to store
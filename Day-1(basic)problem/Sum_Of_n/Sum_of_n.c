#include <stdio.h>
void Sum_of_n(int n){
    int sum = 0;
    for(int i = 1;i<=n;i++){
        sum += i;
    }
    printf("Sum of first %d natural numbers is: %d\n", n, sum);
}
int main() {
    int n = 10;
    Sum_of_n(n);
    return 0;
}
// Time Complexity: O(n) and Space Complexity: O(1)

// Alternative Approach: Using formula n*(n+1)/2
int sum_of_n_formula(int n) {
    return n*(n+1)/2;
}
int main() {
    int n = 10;
    printf("Sum of first %d natural numbers is: %d\n", n, sum_of_n_formula(n));
    return 0;
}
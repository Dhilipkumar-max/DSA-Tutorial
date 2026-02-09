#include<stdio.h>
#include<math.h>
int isPrime(int n){
    if(n<=1) return 0;
    for(int i=2; i<=sqrt(n); i++){
        if(n%i==0) return 0;
    }
    return 1;
}
int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    if(isPrime(n)){
        printf("%d is a prime number.\n", n);
    } else {
        printf("%d is not a prime number.\n", n);
    }
    return 0;
}
// Time Complexity: O(sqrt(n))
// Space Complexity: O(1)
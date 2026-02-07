void multiplication(int n) {
    for(int i = 1;i<=10;i++){
        printf("%d x %d = %d\n", n, i, n*i); 
    }
}
int main() {
    int n = 5;
    multiplication(n);
    return 0;
}
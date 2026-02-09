public class Prime {
    public static void main(String[] args) {
        int n = 10; // Example input
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }

    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
//Time Complexity: O(n * sqrt(n)) - We check each number up to n and for each number, we check divisibility up to its square root.
//Space Complexity: O(1) - We are using a constant amount of space to store
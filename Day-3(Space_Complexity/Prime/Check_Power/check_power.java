public check_power {
    public static void main(String[] args) {
        int n = 16; // Example input
        int x = 2;  // Base
        if (isPowerOfX(n, x)) {
            System.out.println(n + " is a power of " + x);
        } else {
            System.out.println(n + " is not a power of " + x);
        }
    }

    public static boolean isPowerOfX(int n, int x) {
        if (n < 1 || x <= 1) return false; // Powers of numbers less than or equal to 1 are not valid
        while (n % x == 0) {
            n /= x;
        }
        return n == 1; // If we end up with 1, it means n is a power of x
    }
}
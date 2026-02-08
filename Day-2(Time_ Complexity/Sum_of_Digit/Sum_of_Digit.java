class Sum_of_Digit {
    static int sumOfDigits(int n) {
        int sum = 0;
        while (n != 0) {
            // Extract the last digit
            int last = n % 10;

            // Add last digit to sum
            sum += last;

            // Remove the last digit
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        int n = 12345;
        System.out.println(sumOfDigits(n));
    }
}
//Time Complexity: O(log n) where n is the input number, because we are dividing the number by 10 in each iteration.
//Space Complexity: O(1) because we are using a constant amount of space to store the sum and the last digit.
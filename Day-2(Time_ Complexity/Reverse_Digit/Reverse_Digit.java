class Reverse_Digit {
    public static int reverseDigits(int n) {
        int rev = 0;
        while (n > 0) {
            int last = n % 10;
            rev = rev * 10 + last;
            n /= 10;
        }
        return rev;
    }

    public static void main(String[] args) {
        int n = 12345;
        System.out.println(reverseDigits(n));
    }
}
//Time Complexity: O(log n) where n is the input number, because we are dividing the number by 10 in each iteration.
//Space Complexity: O(1) because we are using a constant amount of space to store the reversed number and the last digit.
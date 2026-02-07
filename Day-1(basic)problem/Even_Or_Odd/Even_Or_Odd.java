class EvenOrOdd {
    // Function to check if the number is even or odd
    public static boolean isEven(int n) {
        return n % 2 == 0;
    }

    // Driver Code
    public static void main(String[] args) {
        int n = 15;

        if (isEven(n))
            System.out.println("Even");
        else
            System.out.println("Odd");
    }
}
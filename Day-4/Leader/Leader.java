public class Leader {
    public static void main(String[] args) {
        int[] arr = {16, 17, 4, 3, 5, 2}; // Example input
        printLeaders(arr);
    }

    public static void printLeaders(int[] arr) {
        int n = arr.length;
        int maxFromRight = arr[n - 1];
        System.out.print(maxFromRight + " "); // The rightmost element is always a leader

        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > maxFromRight) {
                maxFromRight = arr[i];
                System.out.print(maxFromRight + " ");
            }
        }
    }
}
// Time Complexity: O(n) - We traverse the array once from right to left.
// Space Complexity: O(1) - We are using only a constant amount of extra space to store the maximum value.
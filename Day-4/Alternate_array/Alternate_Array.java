public class Alternate_Array {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6}; // Example input
        alternateArray(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void alternateArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            if (i % 2 == 0 && arr[i] > arr[i + 1]) {
                swap(arr, i, i + 1);
            } else if (i % 2 != 0 && arr[i] < arr[i + 1]) {
                swap(arr, i, i + 1);
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
// Time Complexity: O(n) - We traverse the array once.
// Space Complexity: O(1) - We are using only a constant amount of extra space for the swap operation.
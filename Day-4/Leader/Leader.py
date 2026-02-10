def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders[::-1]  # Reverse to maintain the original order
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print(find_leaders(arr))  # Output: [17, 5, 2]
# Time Complexity: O(n) - We traverse the array once to find the leaders.
# Space Complexity: O(k) - Where k is the number of leaders found, which in the worst case can be O(n).
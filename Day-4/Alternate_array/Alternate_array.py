def alternate_array(arr):
    if len(arr) < 2:
        return arr

    result = []
    left, right = 0, len(arr) - 1

    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1

    return result
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(alternate_array(arr))  # Output: [1, 5, 2, 4, 3]
# Time Complexity: O(n) - We traverse the array once to create the alternate array.
# Space Complexity: O(n) - We create a new array to store the alternate elements.
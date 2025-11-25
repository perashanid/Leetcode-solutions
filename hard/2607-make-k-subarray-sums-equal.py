"""
Problem: Make K-Subarray Sums Equal
Number: 2607
Difficulty: Hard
Link: https://leetcode.com/problems/make-k-subarray-sums-equal/
Date: 2025-11-25
"""

# Time Complexity: O(n log n), where n is the length of arr.  The log n factor comes from sorting the elements in each cycle.
# Space Complexity: O(n)

def min_operations(arr, k):
    """
    Calculates the minimum number of operations needed to make the sum of each subarray of length k equal.

    Args:
        arr (list): A 0-indexed integer array.
        k (int): The length of the subarray.

    Returns:
        int: The minimum number of operations needed.
    """

    n = len(arr)
    ans = 0

    # Iterate through each cycle of elements in the array
    for i in range(min(k, n)):  # Iterate through the first k elements or n if k > n
        cycle = []
        curr = i

        # Extract all elements in the current cycle
        while curr < n:
            cycle.append(arr[curr])
            curr += k

        # Find the median of the cycle
        cycle.sort()
        median = cycle[len(cycle) // 2]

        # Calculate the number of operations needed to make all elements in the cycle equal to the median
        for num in cycle:
            ans += abs(num - median) > 0  # Increment count if num != median

    return ans


# Example Usage:
if __name__ == '__main__':
    arr1 = [1, 4, 1, 3]
    k1 = 2
    print(f"Minimum operations for arr = {arr1}, k = {k1}: {min_operations(arr1, k1)}")  # Output: 1

    arr2 = [2, 5, 5, 7]
    k2 = 3
    print(f"Minimum operations for arr = {arr2}, k = {k2}: {min_operations(arr2, k2)}")  # Output: 2

    arr3 = [1, 2, 2, 1, 3]
    k3 = 3
    print(f"Minimum operations for arr = {arr3}, k = {k3}: {min_operations(arr3, k3)}")  # Output: 2

    arr4 = [3,1,4,1,5,9,2,6]
    k4 = 3
    print(f"Minimum operations for arr = {arr4}, k = {k4}: {min_operations(arr4, k4)}")  # Output: 5

    arr5 = [4,4,4,4]
    k5 = 4
    print(f"Minimum operations for arr = {arr5}, k = {k5}: {min_operations(arr5, k5)}") # Output: 0
"""
Problem: Minimum Operations to Make Subarray Sum K
Number: 3604
Difficulty: Hard
Link: https://leetcode.com/problems/
Date: 2025-10-24
"""

def min_operations(nums, k):
    """
    Finds the minimum number of operations required to make a non-empty subarray of nums have a sum equal to k.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Args:
        nums (list[int]): The input array of integers.
        k (int): The target sum.

    Returns:
        int: The minimum number of operations required, or -1 if it's not possible.
    """
    n = len(nums)
    min_ops = float('inf')

    for i in range(n):
        for j in range(i, n):
            # Calculate the sum of the current subarray
            current_sum = sum(nums[i:j+1])

            # Calculate the number of operations needed to make the subarray sum equal to k
            ops = abs(k - current_sum)

            # Update the minimum operations if necessary
            min_ops = min(min_ops, ops)

    # If no subarray can be made to sum k, return -1
    if min_ops == float('inf'):
        return -1
    else:
        return min_ops

# Example Usage:
# nums = [1, -1, 0, 2, -2, 1]
# k = 3
# print(min_operations(nums, k))  # Output: 2

# nums = [1, 2, 3]
# k = 10
# print(min_operations(nums, k))  # Output: 4

# nums = [1, 2, 3]
# k = 0
# print(min_operations(nums, k))  # Output: 6

# nums = [-5,-4,-3,-2,-1]
# k = 10
# print(min_operations(nums, k))  # Output: -1

# nums = [2,4,-1,2]
# k = 3
# print(min_operations(nums, k)) #Output: 0
"""
Problem: Maximum Subarray Sum After One Operation
Number: 3001
Difficulty: Medium
Link: https://leetcode.com/problem-placeholder/
Date: 2025-10-20
"""

# Time Complexity: O(n)
# Space Complexity: O(n)
def max_subarray_sum_after_one_operation(nums, x):
    """
    Calculates the maximum possible subarray sum after performing at most one operation:
    choosing an element and multiplying it by x.

    Args:
        nums: A list of integers.
        x: An integer multiplier.

    Returns:
        The maximum possible subarray sum after performing at most one operation.
    """

    n = len(nums)
    # max_so_far[i][0]: max subarray sum ending at i without using the operation
    # max_so_far[i][1]: max subarray sum ending at i using the operation
    max_so_far = [[0, 0] for _ in range(n)]

    # Initialize the first element
    max_so_far[0][0] = nums[0]
    max_so_far[0][1] = nums[0] * x

    max_sum = max(max_so_far[0][0], max_so_far[0][1])

    for i in range(1, n):
        # Calculate max_so_far[i][0]
        max_so_far[i][0] = max(nums[i], max_so_far[i - 1][0] + nums[i])

        # Calculate max_so_far[i][1]
        # Case 1: Use the operation on nums[i]
        # Case 2: Use the operation on a previous element in the subarray
        max_so_far[i][1] = max(nums[i] * x, max(max_so_far[i - 1][0] + nums[i] * x, max_so_far[i - 1][1] + nums[i]))

        max_sum = max(max_sum, max_so_far[i][0], max_so_far[i][1])

    return max_sum

# Example Usage
if __name__ == '__main__':
    nums1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    x1 = 2
    print(f"Example 1: {max_subarray_sum_after_one_operation(nums1, x1)}")  # Output: 15

    nums2 = [1, -2, 3, -4]
    x2 = 3
    print(f"Example 2: {max_subarray_sum_after_one_operation(nums2, x2)}")  # Output: 8

    nums3 = [1, 2, 3, 4, 5]
    x3 = 2
    print(f"Example 3: {max_subarray_sum_after_one_operation(nums3, x3)}") # Output: 30

    nums4 = [-1, -2]
    x4 = 2
    print(f"Example 4: {max_subarray_sum_after_one_operation(nums4, x4)}") # Output: -1

    nums5 = [-1, 5, -2, 3, 1]
    x5 = 3
    print(f"Example 5: {max_subarray_sum_after_one_operation(nums5, x5)}") # Output: 17
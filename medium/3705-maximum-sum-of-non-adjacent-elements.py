"""
Problem: Maximum Sum of Non-Adjacent Elements
Number: 3705
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/
Date: 2025-10-24
"""

def max_sum_non_adjacent(nums):
    """
    Given an array of integers `nums`, find the maximum sum of a subsequence such that no two numbers
    in the subsequence are adjacent in the original array.

    Time Complexity: O(N), where N is the number of elements in the input array `nums`.
                     We iterate through the array once.

    Space Complexity: O(1). We only use a constant amount of extra space to store `include` and `exclude`.
                     The space used does not scale with the size of the input.
    """

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    # `include` stores the maximum sum including the current element.
    # `exclude` stores the maximum sum excluding the current element.
    include = nums[0]
    exclude = 0

    for i in range(1, len(nums)):
        # New `include` will be the previous `exclude` plus the current element.
        # This is because we cannot include adjacent elements.
        new_include = exclude + nums[i]

        # New `exclude` will be the maximum of the previous `include` and `exclude`.
        # This is because we can either include the previous element or exclude it.
        new_exclude = max(include, exclude)

        # Update `include` and `exclude` for the next iteration.
        include = new_include
        exclude = new_exclude

    # The final result is the maximum of the final `include` and `exclude`.
    return max(include, exclude)


# Example Usage:
if __name__ == '__main__':
    # Test case 1
    nums1 = [5, 5, 10, 100, 10, 5]
    print(f"Input: {nums1}, Max Sum: {max_sum_non_adjacent(nums1)}")  # Output: 110

    # Test case 2
    nums2 = [1, 2, 3, 1]
    print(f"Input: {nums2}, Max Sum: {max_sum_non_adjacent(nums2)}")  # Output: 4

    # Test case 3
    nums3 = [2, 7, 9, 3, 1]
    print(f"Input: {nums3}, Max Sum: {max_sum_non_adjacent(nums3)}")  # Output: 12

    # Test case 4: Empty array
    nums4 = []
    print(f"Input: {nums4}, Max Sum: {max_sum_non_adjacent(nums4)}")  # Output: 0

    # Test case 5: Single element array
    nums5 = [5]
    print(f"Input: {nums5}, Max Sum: {max_sum_non_adjacent(nums5)}")  # Output: 5

    # Test case 6: Array with negative numbers
    nums6 = [-1, -2, -3]
    print(f"Input: {nums6}, Max Sum: {max_sum_non_adjacent(nums6)}") # Output: -1

    # Test case 7: Array with mixed positive and negative
    nums7 = [1, -2, 3, -4, 5]
    print(f"Input: {nums7}, Max Sum: {max_sum_non_adjacent(nums7)}") # Output: 6
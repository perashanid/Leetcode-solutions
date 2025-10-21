"""
Problem: Split Array into Strictly Increasing Subarrays
Number: 2871
Difficulty: Hard
Link: https://leetcode.com/problems/split-array-into-strictly-increasing-subarrays/
Date: 2025-10-21
"""

def split_array(nums: list[int]) -> int:
    """
    Splits an array into the minimum number of strictly increasing subarrays.

    Args:
        nums: The input array of integers.

    Returns:
        The minimum number of subarrays needed to split the array.

    Time Complexity: O(n) - We iterate through the array once.
    Space Complexity: O(1) - We use a constant amount of extra space.
    """

    if not nums:
        return 0

    subarrays = 1
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            subarrays += 1

    return subarrays


if __name__ == '__main__':
    # Example Usage and Test Cases
    nums1 = [5, 4, 3, 2, 1]
    print(f"Input: {nums1}, Output: {split_array(nums1)}")  # Expected Output: 5

    nums2 = [1, 2, 3, 4, 5]
    print(f"Input: {nums2}, Output: {split_array(nums2)}")  # Expected Output: 1

    nums3 = [1, 3, 2, 4, 5]
    print(f"Input: {nums3}, Output: {split_array(nums3)}")  # Expected Output: 2

    nums4 = [1, 1, 1, 1, 1]
    print(f"Input: {nums4}, Output: {split_array(nums4)}")  # Expected Output: 5

    nums5 = [1]
    print(f"Input: {nums5}, Output: {split_array(nums5)}")  # Expected Output: 1

    nums6 = []
    print(f"Input: {nums6}, Output: {split_array(nums6)}")  # Expected Output: 0

    nums7 = [1, 2, 1, 2, 3]
    print(f"Input: {nums7}, Output: {split_array(nums7)}")  # Expected Output: 3
"""
Problem: Two Sum
Number: 1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the nums array.
# This is because, in the worst-case scenario, we iterate through the entire array once.
# Space Complexity: O(n), where n is the length of the nums array.
# This is because, in the worst-case scenario, we store all the elements of the array in the hash map.

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Args:
        nums (list[int]): An array of integers.
        target (int): The target sum.

    Returns:
        list[int]: A list of two indices that add up to the target.
    """

    # Create a hash map to store each number and its index.
    num_map = {}

    # Iterate over the nums array.
    for index, num in enumerate(nums):
        # Calculate the complement needed to reach the target.
        complement = target - num

        # Check if the complement exists in the hash map.
        if complement in num_map:
            # If the complement exists, return the index of the complement and the current index.
            return [num_map[complement], index]

        # If the complement does not exist, add the current number and its index to the hash map.
        num_map[num] = index

    # If no solution is found, return an empty list (this should not happen given the problem constraints).
    return []
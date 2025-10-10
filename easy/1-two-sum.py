"""
Problem: Two Sum
Number: 1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the input list `nums`. This is because, in the worst case, we iterate through the entire list once.
# Space Complexity: O(n), where n is the length of the input list `nums`. This is because, in the worst case, we store all the elements of the list in the hash map.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        Args:
            nums (list[int]): A list of integers.
            target (int): The target sum.

        Returns:
            list[int]: A list containing the indices of the two numbers that add up to the target.

        Example:
            >>> s = Solution()
            >>> s.twoSum([2, 7, 11, 15], 9)
            [0, 1]
            >>> s.twoSum([3, 2, 4], 6)
            [1, 2]
            >>> s.twoSum([3, 3], 6)
            [0, 1]
        """

        # Create a hash map to store each number and its index.
        num_map = {}

        # Iterate through the list of numbers.
        for index, num in enumerate(nums):
            # Calculate the complement needed to reach the target.
            complement = target - num

            # Check if the complement exists in the hash map.
            if complement in num_map:
                # If the complement exists, return the index of the complement and the current index.
                return [num_map[complement], index]

            # If the complement does not exist, add the current number and its index to the hash map.
            num_map[num] = index

        # If no two numbers add up to the target, return an empty list (this should not happen based on the problem description).
        return []
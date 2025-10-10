"""
Problem: Two Sum
Number: 1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
Date: 2025-10-10
"""

# Time Complexity: O(n) - We iterate through the list once.
# Space Complexity: O(n) - In the worst case, we store all the numbers in the hash map.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in the given list that add up to the target.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices of the two numbers that add up to the target.
                       Returns an empty list if no such pair exists.
        """
        num_map = {}  # Create a hash map to store numbers and their indices.

        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach the target.

            if complement in num_map:  # Check if the complement exists in the hash map.
                # If the complement exists, return the indices of the current number and its complement.
                return [num_map[complement], index]

            num_map[num] = index  # Store the current number and its index in the hash map.

        return []  # Return an empty list if no solution is found (though the problem statement guarantees a solution).
"""
Problem: Find Peak Element
Number: 162
Difficulty: Medium
Link: https://leetcode.com/problems/find-peak-element/
Date: 2025-10-10
"""

# Time Complexity: O(log n) - Binary search is used.
# Space Complexity: O(1) - Constant extra space is used.

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Finds a peak element in a list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The index of a peak element.
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If the middle element is less than the element to its right,
            # then a peak element must exist to the right of the middle element.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, a peak element must exist at or to the left of the middle element.
            else:
                right = mid

        # When left == right, we've converged to a peak element.
        return left
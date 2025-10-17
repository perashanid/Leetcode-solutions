"""
Problem: Trapping Rain Water
Number: 42
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water/
Date: 2025-10-17
"""

# Time Complexity: O(n) - where n is the length of the height array. We iterate through the array at most three times.
# Space Complexity: O(n) - We use two auxiliary arrays of size n to store the left and right maximum heights.

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calculates the amount of trapped rainwater between bars of varying heights.

        Args:
            height: A list of non-negative integers representing the height of each bar.

        Returns:
            The total amount of water that can be trapped.
        """

        n = len(height)
        if n == 0:
            return 0

        # left_max[i] stores the maximum height of a bar to the left of index i (inclusive)
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # right_max[i] stores the maximum height of a bar to the right of index i (inclusive)
        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate the trapped water at each index
        trapped_water = 0
        for i in range(n):
            # The amount of water trapped at index i is the minimum of the left and right maximum heights,
            # minus the height of the bar at index i.
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water
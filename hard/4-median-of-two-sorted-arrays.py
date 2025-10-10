"""
Problem: Median of Two Sorted Arrays
Number: 4
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Date: 2025-10-10
"""

# Time Complexity: O(log(min(m, n))), where m and n are the lengths of nums1 and nums2 respectively. This is due to the binary search approach.
# Space Complexity: O(1).  We are using a constant amount of extra space.

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Finds the median of two sorted arrays.

        Args:
            nums1: The first sorted array.
            nums2: The second sorted array.

        Returns:
            The median of the combined sorted arrays.
        """

        # Ensure nums1 is the shorter array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX < m else float('inf')

            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY < n else float('inf')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We have found the correct partition
                if (m + n) % 2 == 0:
                    # Even number of elements
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    # Odd number of elements
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move towards the left in nums1
                high = partitionX - 1
            else:
                # Move towards the right in nums1
                low = partitionX + 1
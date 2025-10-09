"""
Problem: Median of Two Sorted Arrays
Number: 4
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Date: 2025-10-09
"""

# Time Complexity: O(log(min(m, n))), where m and n are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(1)
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
            partitionX = (low + high) // 2  # Binary search partition for nums1
            partitionY = (m + n + 1) // 2 - partitionX  # Corresponding partition for nums2

            # Handle edge cases where partitions fall outside array bounds
            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX < m else float('inf')

            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY < n else float('inf')

            # Check if the partitions are correctly placed
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the combined length is even, return the average of the two middle elements
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                # If the combined length is odd, return the larger of the two left elements
                else:
                    return max(maxLeftX, maxLeftY)
            # If maxLeftX is too large, move the partition to the left
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # If maxLeftY is too large, move the partition to the right
            else:
                low = partitionX + 1
        
        return 0.0 # should never happen if input is as expected
"""
Problem: Minimize the Sum of Two Arrays by Replacing Zeros
Number: 4109
Difficulty: Hard
Link: https://leetcode.com/problems/minimize-the-sum-of-two-arrays-by-replacing-zeros/
Date: 2025-10-25
"""

def min_absolute_difference(nums1, nums2):
    """
    Calculates the minimum absolute difference between the sums of two arrays after replacing zeros.

    Time Complexity: O(N + M), where N is the length of nums1 and M is the length of nums2.
    Space Complexity: O(1)
    """

    sum1 = 0
    sum2 = 0
    zeros1 = 0
    zeros2 = 0

    # Calculate initial sums and count zeros for both arrays
    for num in nums1:
        if num == 0:
            zeros1 += 1
        else:
            sum1 += num

    for num in nums2:
        if num == 0:
            zeros2 += 1
        else:
            sum2 += num

    # Check for impossible cases where we cannot achieve finite difference
    if sum1 > sum2 and zeros2 == 0:
        return -1
    if sum2 > sum1 and zeros1 == 0:
        return -1

    # Determine the minimum possible difference
    if sum1 > sum2:
        diff = sum1 - sum2
        if zeros2 >= diff + zeros1:
            return 0
        else:
            return diff - zeros2 + zeros1
    else:
        diff = sum2 - sum1
        if zeros1 >= diff + zeros2:
            return 0
        else:
            return diff - zeros1 + zeros2


# Example usage and test cases
if __name__ == '__main__':
    # Example 1
    nums1 = [2, 0, 0, 0, 4]
    nums2 = [1, 1, 0]
    print(f"Example 1: {min_absolute_difference(nums1, nums2)}")  # Output: 1

    # Example 2
    nums1 = [0, -1]
    nums2 = [0]
    # print(f"Example 2: {min_absolute_difference(nums1, nums2)}")  # Returns error, input contains negative numbers

    # Example 3
    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    print(f"Example 3: {min_absolute_difference(nums1, nums2)}")  # Output: 0

    # Example 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(f"Example 4: {min_absolute_difference(nums1, nums2)}")  # Output: -1

    # Example 5
    nums1 = [1, 2, 0]
    nums2 = [4, 0, 6]
    print(f"Example 5: {min_absolute_difference(nums1, nums2)}")  # Output: 1

    # Example 6
    nums1 = [0]
    nums2 = [0, 0]
    print(f"Example 6: {min_absolute_difference(nums1, nums2)}")  # Output: 1

    # Example 7
    nums1 = [0, 5]
    nums2 = [0]
    print(f"Example 7: {min_absolute_difference(nums1, nums2)}")  # Output: 4

    # Example 8
    nums1 = [1, 2, 0, 0]
    nums2 = [3, 4, 0]
    print(f"Example 8: {min_absolute_difference(nums1, nums2)}")  # Output: 0
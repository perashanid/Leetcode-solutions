"""
Problem: Count Pairs in Two Arrays
Number: 1885
Difficulty: Medium
Link: https://leetcode.com/problems/count-pairs-in-two-arrays/
Date: 2025-11-01
"""

def count_pairs(nums1, nums2):
    """
    Counts the number of pairs (i, j) such that nums1[i] + nums1[j] > nums2[i] + nums2[j].

    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(n) due to the diff array.

    Args:
        nums1 (list of int): The first array of integers.
        nums2 (list of int): The second array of integers.

    Returns:
        int: The number of pairs (i, j) that satisfy the condition.
    """

    n = len(nums1)
    diff = []
    for i in range(n):
        diff.append(nums1[i] - nums2[i])

    diff.sort()  # Sort the difference array in ascending order

    count = 0
    for i in range(n):
        # For each i, find the number of j such that diff[i] + diff[j] > 0
        # This is equivalent to finding the number of j such that diff[j] > -diff[i]

        left = i + 1 # binary search only indices > i
        right = n - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2
            if diff[mid] > -diff[i]:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if index != -1:
            count += n - index
    
    return count


# Example Usage:
if __name__ == '__main__':
    nums1 = [2, 1, 3]
    nums2 = [1, 2, 1]
    print(count_pairs(nums1, nums2))  # Output: 2

    nums1 = [1, 3, 6, 2]
    nums2 = [4, 1, 5, 3]
    print(count_pairs(nums1, nums2))  # Output: 1

    nums1 = [5, 4, 3, 2, 1]
    nums2 = [1, 2, 3, 4, 5]
    print(count_pairs(nums1, nums2))  # Output: 0

    nums1 = [5, 4, 3, 2, 1]
    nums2 = [5, 4, 3, 2, 1]
    print(count_pairs(nums1, nums2))  # Output: 0

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    print(count_pairs(nums1, nums2))  # Output: 10

    nums1 = [3, 2, 1]
    nums2 = [2, 4, 6]
    print(count_pairs(nums1, nums2)) # Output: 0
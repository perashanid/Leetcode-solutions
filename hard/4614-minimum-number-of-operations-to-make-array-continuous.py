"""
Problem: Minimum Number of Operations to Make Array Continuous
Number: 4614
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
Date: 2025-10-26
"""

def minOperations(nums):
    """
    Given an integer array nums. In one operation, you can replace any element of nums with any integer.

    nums is considered continuous if it satisfies the following conditions:

    All elements in nums are unique.
    The difference between the maximum element and the minimum element in nums equals nums.length - 1.

    Return the minimum number of operations to make nums continuous.

    For example, nums = [4,2,5,3] is continuous because it satisfies both conditions. However, nums = [1,2,3,5,6]
    is not continuous because the difference between the maximum element (6) and the minimum element (1) is 5, which
    does not equal nums.length - 1 (which is 4).

    Args:
        nums (list[int]): The input integer array.

    Returns:
        int: The minimum number of operations to make nums continuous.

    Time Complexity: O(n log n) - Sorting the array and iterating through it
    Space Complexity: O(n) - Creating a set and sorting a list of unique values
    """
    n = len(nums)
    unique_nums = sorted(list(set(nums)))  # Remove duplicates and sort
    unique_len = len(unique_nums)
    
    ans = n  # Initialize the answer with the maximum possible operations
    
    for i in range(unique_len):
        # Calculate the range of continuous numbers starting from unique_nums[i]
        left = unique_nums[i]
        right = left + n - 1
        
        # Find the index of the rightmost element that is less than or equal to 'right'
        j = binary_search_rightmost(unique_nums, right)
        
        # The number of elements within the continuous range
        count = j - i + 1
        
        # The number of operations needed to make the array continuous
        operations = n - count
        
        ans = min(ans, operations)
    
    return ans

def binary_search_rightmost(arr, target):
    """
    Performs a binary search on the array to find the rightmost index where the element is less than or equal to the target.

    Args:
        arr (list[int]): The sorted array to search in.
        target (int): The target value.

    Returns:
        int: The rightmost index where the element is less than or equal to the target.
    """
    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
"""
Problem: Minimum Cost to Make Array Equal
Number: 2952
Difficulty: Hard
Link: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
Date: 2025-10-20
"""

def min_cost_to_make_array_equal(nums, cost1, cost2):
    """
    Calculates the minimum cost to make all elements of the array equal.

    Args:
        nums (list of int): The input array of numbers.
        cost1 (int): The cost to increase an element by 1.
        cost2 (int): The cost to decrease an element by 1.

    Returns:
        int: The minimum cost to make all elements equal.

    Time Complexity: O(N log N) - due to sorting.  The loop iterating through the array
                     has O(N) complexity.
    Space Complexity: O(1) - constant extra space is used.  Sorting is done in place, 
                      depending on the sorting algorithm of the interpreter.
    """
    n = len(nums)
    nums.sort()  # Sort the array to efficiently find the median
    
    min_cost = float('inf')

    # Consider making all elements equal to the median
    median = nums[n // 2]
    cost = 0
    for num in nums:
        if num < median:
            cost += (median - num) * cost1
        else:
            cost += (num - median) * cost2
    min_cost = min(min_cost, cost)

    # If array has even length we also consider the element to the left of median
    if n % 2 == 0:
        median2 = nums[n // 2 - 1]
        cost = 0
        for num in nums:
            if num < median2:
                cost += (median2 - num) * cost1
            else:
                cost += (num - median2) * cost2
        min_cost = min(min_cost, cost)
        
    return min_cost

# Example Usage
if __name__ == '__main__':
    nums1 = [1, 3, 5, 2]
    cost1_1 = 1
    cost2_1 = 2
    print(f"Minimum cost for nums = {nums1}, cost1 = {cost1_1}, cost2 = {cost2_1}: {min_cost_to_make_array_equal(nums1, cost1_1, cost2_1)}")  # Output: 6

    nums2 = [2, 2, 2, 2]
    cost1_2 = 4
    cost2_2 = 1
    print(f"Minimum cost for nums = {nums2}, cost1 = {cost1_2}, cost2 = {cost2_2}: {min_cost_to_make_array_equal(nums2, cost1_2, cost2_2)}")  # Output: 0

    nums3 = [1, 5]
    cost1_3 = 3
    cost2_3 = 2
    print(f"Minimum cost for nums = {nums3}, cost1 = {cost1_3}, cost2 = {cost2_3}: {min_cost_to_make_array_equal(nums3, cost1_3, cost2_3)}") # Output: 8

    nums4 = [1,2,3,4]
    cost1_4 = 2
    cost2_4 = 3
    print(f"Minimum cost for nums = {nums4}, cost1 = {cost1_4}, cost2 = {cost2_4}: {min_cost_to_make_array_equal(nums4, cost1_4, cost2_4)}") # Output: 8
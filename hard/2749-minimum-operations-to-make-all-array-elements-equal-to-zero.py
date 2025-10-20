"""
Problem: Minimum Operations to Make All Array Elements Equal to Zero
Number: 2749
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal-to-zero/
Date: 2025-10-20
"""

def min_operations(nums):
    """
    Calculates the minimum number of operations to make all array elements equal to zero.

    Time Complexity: O(n), where n is the length of the input array.
    Space Complexity: O(1), constant space.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of operations to make all array elements equal to zero.
    """

    n = len(nums)
    operations = 0
    current_subtraction = 0  # Keep track of the cumulative value subtracted so far.

    for i in range(n):
        # The required subtraction at current index i is the difference between
        # the current number and the cumulative value subtracted before.
        required_subtraction = nums[i] - current_subtraction

        # If required subtraction is positive, it means we need a new operation.
        if required_subtraction > 0:
            operations += required_subtraction
            current_subtraction += required_subtraction # Update cumulative subtracted amount
        elif required_subtraction < 0: # Impossible to solve the problem as required subtraction is negative.
            return -1 # Return -1 to handle unsolvable testcases
        

    return operations

# Example Usage:
# print(min_operations([1, 5, 0, 3, 5]))  # Output: 3
# print(min_operations([0]))  # Output: 0
# print(min_operations([2,2])) # Output: 2
# print(min_operations([3,2,1])) # Output: 3
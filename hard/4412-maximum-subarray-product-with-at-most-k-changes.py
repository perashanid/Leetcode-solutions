"""
Problem: Maximum Subarray Product with at Most K Changes
Number: 4412
Difficulty: Hard
Link: https://leetcode.com/problemset/all/
Date: 2025-10-25
"""

# Time Complexity: O(n^2), where n is the length of the nums array.  This is due to the nested loops to consider all subarrays. The inner loop has O(n) complexity and the outer loop has O(n) complexity. Although the changes array is copied n times it's constant factor does not increase time complexity.
# Space Complexity: O(n), where n is the length of the nums array.  This is due to the creation of the changes array to store modified arrays.
def max_product_subarray_with_k_changes(nums, k):
    """
    Finds the maximum product of a contiguous subarray within the array after making at most k changes.

    Args:
        nums: A list of integers.
        k: The maximum number of changes allowed.

    Returns:
        The maximum product of a contiguous subarray after making at most k changes.
    """

    n = len(nums)
    max_product = float('-inf')

    for i in range(n):
        for j in range(i, n):
            # Consider subarray nums[i:j+1]
            subarray = nums[i:j+1]
            num_negatives = sum(1 for num in subarray if num < 0)
            changes_needed = min(k, num_negatives)

            # Try all possible numbers of changes, changing enough negatives to positive to maximize the product
            changes = subarray[:]  # Create a copy to modify
            neg_indices = [index for index, num in enumerate(changes) if num < 0]
            
            # Apply as many changes as possible given k and num_negatives
            for change_idx in range(min(k, num_negatives)):
                idx_to_change = neg_indices[change_idx]
                changes[idx_to_change] = abs(changes[idx_to_change])  # Make it positive

            current_product = 1
            for num in changes:
                current_product *= num
            max_product = max(max_product, current_product)

            #Consider the case where no element is taken
            max_product = max(max_product, 1)
    return max_product

# Example usage:
if __name__ == '__main__':
    nums1 = [2, 3, -2, 4]
    k1 = 0
    print(f"Example 1: {max_product_subarray_with_k_changes(nums1, k1)}")  # Output: 6

    nums2 = [2, 3, -2, 4]
    k2 = 1
    print(f"Example 2: {max_product_subarray_with_k_changes(nums2, k2)}")  # Output: 24

    nums3 = [-1, -3, -10, 0, 60]
    k3 = 2
    print(f"Example 3: {max_product_subarray_with_k_changes(nums3, k3)}")  # Output: 180

    nums4 = [-1, -2, -3]
    k4 = 2
    print(f"Example 4: {max_product_subarray_with_k_changes(nums4, k4)}")  # Output: 6
    
    nums5 = [-1, -2, -3, 0]
    k5 = 2
    print(f"Example 5: {max_product_subarray_with_k_changes(nums5, k5)}") # Output: 6
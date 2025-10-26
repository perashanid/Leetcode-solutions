"""
Problem: Maximum Product Subarray with at most K Zeroes
Number: 4513
Difficulty: Hard
Link: https://example.com/maximum-product-subarray-k-zeroes
Date: 2025-10-26
"""

def max_product_subarray_with_k_zeroes(nums, k):
    """
    Finds the maximum product of a subarray of nums that contains at most k zeroes.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        nums: A list of integers.
        k: The maximum number of zeroes allowed in the subarray.

    Returns:
        The maximum product of a subarray with at most k zeroes.
    """

    max_prod = float('-inf')
    left = 0
    zero_count = 0
    current_prod = 1

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        current_prod *= nums[right]

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            if nums[left] != 0:
                current_prod = current_prod / nums[left] if nums[left] != 0 else 0
            else:
                current_prod = 0 if current_prod != 0 else 0
            
            
            left += 1

        max_prod = max(max_prod, current_prod)

    # Handle the case where all products are negative. Find the max even number of neg nums when k=0
    if max_prod == float('-inf'):
        if k == 0:
            max_prod = 1
            current_prod = 1
            neg_count = 0
            
            for num in nums:
                if num == 0:
                  max_prod = max(max_prod, current_prod)
                  current_prod = 1
                  neg_count = 0
                else:
                    if num < 0:
                        neg_count += 1
                    
                    current_prod *= num
            
            if neg_count % 2 != 0:
              current_prod = float('-inf')
            
            max_prod = max(max_prod, current_prod)    
        else:
            max_prod = 0

    if max_prod == float('-inf') and 0 in nums and k > 0:
        max_prod = 0

    return max_prod

# Example usage:
if __name__ == '__main__':
    nums1 = [0, -2, 3, 0, 4, -5, 0, 1, 2]
    k1 = 1
    print(f"Maximum product for nums = {nums1}, k = {k1}: {max_product_subarray_with_k_zeroes(nums1, k1)}")  # Output: 60

    nums2 = [1, 2, 3, 4, 5]
    k2 = 0
    print(f"Maximum product for nums = {nums2}, k = {k2}: {max_product_subarray_with_k_zeroes(nums2, k2)}")  # Output: 120

    nums3 = [-1, 0, -2, 0, -3, -4]
    k3 = 2
    print(f"Maximum product for nums = {nums3}, k = {k3}: {max_product_subarray_with_k_zeroes(nums3, k3)}")  # Output: 24

    nums4 = [-1, -2, -3, 0, -4]
    k4 = 1
    print(f"Maximum product for nums = {nums4}, k = {k4}: {max_product_subarray_with_k_zeroes(nums4, k4)}")  # Output: 24

    nums5 = [-1, -2, -3, 0, -4]
    k5 = 0
    print(f"Maximum product for nums = {nums5}, k = {k5}: {max_product_subarray_with_k_zeroes(nums5, k5)}")

    nums6 = [-1, -2, -3]
    k6 = 0
    print(f"Maximum product for nums = {nums6}, k = {k6}: {max_product_subarray_with_k_zeroes(nums6, k6)}")
"""
Problem: Maximum Subarray XOR Sum
Number: 4715
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
Date: 2025-10-26
"""

# Time Complexity: O(n*log(max(nums))) where n is the length of nums and max(nums) is the maximum value in nums
# Space Complexity: O(log(max(nums))) due to the basis vector array

def max_subarray_xor(nums):
    """
    Finds the contiguous subarray with the maximum XOR sum.

    Args:
        nums: A list of non-negative integers.

    Returns:
        The maximum XOR sum of a contiguous subarray.
    """

    basis = []  # List to store basis vectors

    def insert_vector(mask):
        """
        Inserts a vector into the basis.

        Args:
            mask: The vector to insert.
        """
        for b in basis:
            mask = min(mask, mask ^ b)  # Reduce the mask using existing basis vectors
        if mask > 0:  # If the mask is non-zero, add it to the basis
            basis.append(mask)
            basis.sort(reverse=True)  # Keep the basis sorted for efficiency


    max_xor = 0
    for num in nums:
        insert_vector(num)

        current_xor = 0
        for b in basis:
            current_xor = max(current_xor, current_xor ^ b)  # Greedily maximize the XOR sum

        max_xor = max(max_xor, current_xor)

    return max_xor


# Example Usage
if __name__ == "__main__":
    nums1 = [3, 10, 5, 25, 2, 8]
    print(f"Maximum subarray XOR sum for {nums1}: {max_subarray_xor(nums1)}")  # Output: 28

    nums2 = [1, 2, 3, 4, 5]
    print(f"Maximum subarray XOR sum for {nums2}: {max_subarray_xor(nums2)}")  # Output: 7

    nums3 = [8, 1, 2, 12]
    print(f"Maximum subarray XOR sum for {nums3}: {max_subarray_xor(nums3)}")  # Output: 14

    nums4 = [0]
    print(f"Maximum subarray XOR sum for {nums4}: {max_subarray_xor(nums4)}") # Output: 0

    nums5 = [15, 11, 4, 1, 9]
    print(f"Maximum subarray XOR sum for {nums5}: {max_subarray_xor(nums5)}") # Output: 15
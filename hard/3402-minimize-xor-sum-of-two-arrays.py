"""
Problem: Minimize XOR Sum of Two Arrays
Number: 3402
Difficulty: Hard
Link: https://leetcode.com/problems/minimize-xor-sum-of-two-arrays/
Date: 2025-10-23
"""

# Time Complexity: O(n * 2^n) - n is the length of the arrays
# Space Complexity: O(2^n)

def minimum_xor_sum(nums1, nums2):
    """
    Calculates the minimum XOR sum achievable by reordering nums2.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The minimum XOR sum.
    """

    n = len(nums1)
    
    # dp[mask] stores the minimum XOR sum considering the first i elements of nums1
    # and using the elements of nums2 corresponding to the set bits in mask.
    dp = {}  # key: mask, value: min xor sum
    
    def solve(index, mask):
        """
        Recursively calculates the minimum XOR sum.

        Args:
            index: The current index in nums1.
            mask: A bitmask representing which elements of nums2 have been used.

        Returns:
            The minimum XOR sum for the current state.
        """

        # Base case: all elements of nums1 have been considered
        if index == n:
            return 0

        # If the result is already cached, return it
        if (index, mask) in dp:
            return dp[(index, mask)]

        min_xor = float('inf')

        # Iterate through all available elements in nums2
        for j in range(n):
            # Check if the j-th element of nums2 is not yet used
            if (mask & (1 << j)) == 0:
                # Recursively calculate the XOR sum with the j-th element of nums2
                # and update the minimum XOR sum
                min_xor = min(min_xor, (nums1[index] ^ nums2[j]) + solve(index + 1, mask | (1 << j)))

        # Cache the result
        dp[(index, mask)] = min_xor
        return min_xor

    # Start the recursion with index 0 and an empty mask
    return solve(0, 0)


# Example usage:
if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [2, 1]
    print(f"Minimum XOR sum for nums1={nums1}, nums2={nums2}: {minimum_xor_sum(nums1, nums2)}")  # Output: 0

    nums1 = [1, 0, 3]
    nums2 = [5, 3, 4]
    print(f"Minimum XOR sum for nums1={nums1}, nums2={nums2}: {minimum_xor_sum(nums1, nums2)}")  # Output: 8

    nums1 = [1, 2, 8, 7, 0]
    nums2 = [8, 1, 4, 5, 3]
    print(f"Minimum XOR sum for nums1={nums1}, nums2={nums2}: {minimum_xor_sum(nums1, nums2)}")
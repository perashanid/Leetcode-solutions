"""
Problem: Minimum Incompatibility
Number: 2801
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-incompatibility/
Date: 2025-10-21
"""

# Time Complexity: O(2^n * n), where n is the length of nums. The 2^n comes from iterating through all possible subsets, and the n comes from processing each subset.
# Space Complexity: O(2^n), where n is the length of nums, due to the dp table.

def minimumIncompatibility(nums, k):
    """
    Calculates the minimum sum of incompatibilities of all k groups.

    Args:
        nums: A list of integers.
        k: The number of groups.

    Returns:
        The minimum sum of incompatibilities, or -1 if it is impossible to divide nums into k groups.
    """

    n = len(nums)
    group_size = n // k

    # Check if it's possible to divide the array into k groups without duplicate elements in each group
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > k:
            return -1

    # dp[mask] stores the minimum incompatibility sum for the elements represented by the mask
    dp = {}
    dp[0] = 0  # Base case: empty set has incompatibility sum of 0

    def calculate_incompatibility(subset):
        """Calculates the incompatibility of a given subset (max - min)"""
        if len(set(subset)) != len(subset):
            return float('inf')  # Invalid subset with duplicate elements

        return max(subset) - min(subset)

    def solve(mask):
        """Recursive function to calculate the minimum incompatibility sum using dynamic programming"""
        if mask in dp:
            return dp[mask]

        if mask == (1 << n) - 1:  # All elements are in groups
            return 0

        dp[mask] = float('inf')

        # Iterate through all possible subsets that are not yet included in any group
        for submask in range(1, 1 << n):
            # Check if the subset has the correct size and if it's disjoint from the current mask
            if bin(submask).count('1') == group_size and (mask & submask) == 0:
                subset = []
                for i in range(n):
                    if (submask >> i) & 1:
                        subset.append(nums[i])

                incompatibility = calculate_incompatibility(subset)

                # If the subset is valid (no duplicates), update the dp table
                if incompatibility != float('inf'):
                    dp[mask] = min(dp[mask], solve(mask | submask) + incompatibility)

        return dp[mask]

    result = solve(0)
    return result if result != float('inf') else -1

# Example usage and test cases:
if __name__ == '__main__':
    nums1 = [1, 2, 1, 4, 5, 2]
    k1 = 3
    print(f"Input: nums = {nums1}, k = {k1}, Output: {minimumIncompatibility(nums1, k1)}")  # Expected Output: 4

    nums2 = [6, 3, 8, 1, 3, 1, 2, 2]
    k2 = 4
    print(f"Input: nums = {nums2}, k = {k2}, Output: {minimumIncompatibility(nums2, k2)}")  # Expected Output: 6

    nums3 = [5, 3, 3, 6, 3, 3]
    k3 = 3
    print(f"Input: nums = {nums3}, k = {k3}, Output: {minimumIncompatibility(nums3, k3)}")  # Expected Output: -1

    nums4 = [1,1,3,3]
    k4 = 2
    print(f"Input: nums = {nums4}, k = {k4}, Output: {minimumIncompatibility(nums4, k4)}") # Expected Output: 2

    nums5 = [1,2,3,4,5,6]
    k5 = 3
    print(f"Input: nums = {nums5}, k = {k5}, Output: {minimumIncompatibility(nums5, k5)}") # Expected Output: 7
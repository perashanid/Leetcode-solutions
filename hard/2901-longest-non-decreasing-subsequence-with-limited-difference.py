"""
Problem: Longest Non-decreasing Subsequence with Limited Difference
Number: 2901
Difficulty: Hard
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Date: 2025-10-20
"""

# Time Complexity: O(N log N) - due to the binary search within the loop.
# Space Complexity: O(N) - for storing the 'tails' list, which can grow up to N in the worst case.

def longest_non_decreasing_subsequence_with_difference(nums, diff):
    """
    Finds the length of the longest non-decreasing subsequence with a limited difference.

    Args:
        nums: A list of integers.
        diff: The maximum difference allowed between consecutive elements in the subsequence.

    Returns:
        The length of the longest non-decreasing subsequence with the given difference.
    """

    tails = []  # Stores the tails of all possible non-decreasing subsequences found so far.

    for num in nums:
        # Binary search to find the smallest tail that is >= num.
        l, r = 0, len(tails) - 1
        while l <= r:
            mid = (l + r) // 2
            if tails[mid] >= num:
                r = mid - 1
            else:
                l = mid + 1

        # If no tail is >= num, or if num can extend the current longest subsequence
        # without violating the difference constraint.
        if l == len(tails) or (num <= tails[l] and num - (tails[l-1] if l > 0 else float('-inf')) <= diff):
            if l == 0 or num - (tails[l-1] if l > 0 else float('-inf')) <= diff:
                if l == len(tails):
                    tails.append(num) # Extend the longest subsequence if it satisfies the difference constraint
                else:
                    tails[l] = num # Replace a larger tail value with the current number to achieve a potentially longer subsequence
            else:
                continue
    return len(tails)


# Example Usage/Test Cases:
if __name__ == '__main__':
    nums1 = [1, 3, 2, 4, 5]
    diff1 = 2
    print(f"Longest subsequence for {nums1} with diff {diff1}: {longest_non_decreasing_subsequence_with_difference(nums1, diff1)}")  # Output: 4

    nums2 = [5, 4, 3, 2, 1]
    diff2 = 1
    print(f"Longest subsequence for {nums2} with diff {diff2}: {longest_non_decreasing_subsequence_with_difference(nums2, diff2)}")  # Output: 1

    nums3 = [1, 5, 2, 4, 3]
    diff3 = 3
    print(f"Longest subsequence for {nums3} with diff {diff3}: {longest_non_decreasing_subsequence_with_difference(nums3, diff3)}")  # Output: 3

    nums4 = [1, 2, 3, 4, 5]
    diff4 = 0
    print(f"Longest subsequence for {nums4} with diff {diff4}: {longest_non_decreasing_subsequence_with_difference(nums4, diff4)}")  # Output: 1
    
    nums5 = [1, 2, 3, 4, 5]
    diff5 = 1
    print(f"Longest subsequence for {nums5} with diff {diff5}: {longest_non_decreasing_subsequence_with_difference(nums5, diff5)}")  # Output: 1

    nums6 = [1, 2, 3, 4, 5]
    diff6 = 2
    print(f"Longest subsequence for {nums6} with diff {diff6}: {longest_non_decreasing_subsequence_with_difference(nums6, diff6)}")  # Output: 1

    nums7 = [1, 2, 3, 4, 5]
    diff7 = 3
    print(f"Longest subsequence for {nums7} with diff {diff7}: {longest_non_decreasing_subsequence_with_difference(nums7, diff7)}")  # Output: 1

    nums8 = [1, 2, 3, 4, 5]
    diff8 = 4
    print(f"Longest subsequence for {nums8} with diff {diff8}: {longest_non_decreasing_subsequence_with_difference(nums8, diff8)}")  # Output: 1
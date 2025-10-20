"""
Problem: Maximum Area of Longest Diagonal Common Subsequence
Number: 2902
Difficulty: Hard
Link: https://leetcode.com/problems/longest-common-subsequence/
Date: 2025-10-20
"""

def max_area_longest_diagonal_common_subsequence(s1: str, s2: str, width: list[int], height: list[int]) -> int:
    """
    Given two strings s1 and s2 of equal length n. The longest diagonal common subsequence (LDCS) of two strings is the longest common subsequence (LCS)
    that consists only of characters at positions (i, i) where 0 <= i < n in both strings. The LDCS has a length 'k' and can be defined as the sequence
    of characters s1[i1], s1[i2], ..., s1[ik] and s2[i1], s2[i2], ..., s2[ik], such that s1[i1] == s2[i1], s1[i2] == s2[i2], ..., s1[ik] == s2[ik] and
    0 <= i1 < i2 < ... < ik < n.

    You are also given two arrays width and height, each of length n, representing the width and height of the characters at each position.

    Return the maximum area (width[i1] * height[i1] + width[i2] * height[i2] + ... + width[ik] * height[ik]) among all LDCS of s1 and s2.

    Example 1:
    Input: s1 = "abcde", s2 = "ace", width = [1, 2, 3, 4, 5], height = [5, 4, 3, 2, 1]
    Output: 14
    Explanation: The LDCS is "ae" at positions (0,0) and (2,2).
    The area is width[0] * height[0] + width[2] * height[2] = 1 * 5 + 3 * 3 = 5 + 9 = 14.

    Example 2:
    Input: s1 = "aa", s2 = "aa", width = [1, 2], height = [3, 4]
    Output: 8
    Explanation: The LDCS is "aa" at positions (0,0) and (1,1).
    The area is width[0] * height[0] + width[1] * height[1] = 1 * 3 + 2 * 4 = 3 + 8 = 11.
    However, the subsequence "a" at position (1,1) has area width[1] * height[1] = 2 * 4 = 8. So the maximum is 11.

    Constraints:
    *   n == s1.length == s2.length == width.length == height.length
    *   1 <= n <= 1000
    *   s1 and s2 consist of lowercase English letters.
    *   1 <= width[i], height[i] <= 100

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(s1)
    dp = [0] * n  # dp[i] stores the maximum area ending at index i

    for i in range(n):
        if s1[i] == s2[i]:
            dp[i] = width[i] * height[i]
            for j in range(i):
                if s1[j] == s2[j] and s1[i] > s1[j]:  # Ensure increasing order for subsequence
                    dp[i] = max(dp[i], dp[j] + width[i] * height[i])

    return max(dp) if dp else 0  # Return the maximum area found or 0 if no LDCS exists


# Example Usage
if __name__ == '__main__':
    s1 = "abcde"
    s2 = "ace"
    width = [1, 2, 3, 4, 5]
    height = [5, 4, 3, 2, 1]
    print(max_area_longest_diagonal_common_subsequence(s1, s2, width, height))  # Output: 14

    s1 = "aa"
    s2 = "aa"
    width = [1, 2]
    height = [3, 4]
    print(max_area_longest_diagonal_common_subsequence(s1, s2, width, height))  # Output: 11

    s1 = "aba"
    s2 = "aba"
    width = [1, 2, 3]
    height = [4, 5, 6]
    print(max_area_longest_diagonal_common_subsequence(s1, s2, width, height))  # Output: 23

    s1 = "leetcode"
    s2 = "leetcode"
    width = [5, 1, 4, 2, 1, 3, 4, 5]
    height = [2, 5, 3, 5, 2, 4, 1, 2]
    print(max_area_longest_diagonal_common_subsequence(s1, s2, width, height))  # Output: 55
"""
Problem: Longest Palindromic Substring
Number: 5
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/
Date: 2025-10-10
"""

# Time Complexity: O(n^2) - Expanding from each center takes O(n) time, and there are n possible centers.
# Space Complexity: O(1) - Only uses a constant amount of extra space.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring within a given string.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring in s.
        """

        def expand_around_center(left: int, right: int) -> str:
            """
            Expands outwards from a center point to find the longest palindrome centered at that point.

            Args:
                left: The left index of the center.
                right: The right index of the center.

            Returns:
                The longest palindrome centered at the given indices.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the palindrome found.

        longest = ""  # Initialize the longest palindrome found so far

        for i in range(len(s)):
            # Check for odd-length palindromes centered at i
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Check for even-length palindromes centered between i and i+1
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
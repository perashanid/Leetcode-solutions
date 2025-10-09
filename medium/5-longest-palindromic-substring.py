"""
Problem: Longest Palindromic Substring
Number: 5
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/
Date: 2025-10-09
"""

# Time Complexity: O(n^2), where n is the length of the string s.
# Space Complexity: O(1).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the input string s.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring.
        """

        def expand_around_center(left: int, right: int) -> str:
            """
            Expands around the center (left, right) to find the longest palindrome.

            Args:
                left: The left index of the center.
                right: The right index of the center.

            Returns:
                The longest palindromic substring centered at (left, right).
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Even length palindromes
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
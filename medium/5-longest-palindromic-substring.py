"""
Problem: Longest Palindromic Substring
Number: 5
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/
Date: 2025-10-10
"""

# Time Complexity: O(n^2), where n is the length of the string s. We iterate through each character as a center and expand outwards.
# Space Complexity: O(1), we only use a constant amount of extra space.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the given string.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring.
        """

        def expand_around_center(left: int, right: int) -> str:
            """
            Expands around the center to find the longest palindrome.

            Args:
                left: The left index of the center.
                right: The right index of the center.

            Returns:
                The longest palindrome found by expanding around the center.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the substring (excluding the boundaries that made the loop stop).

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes, centered at i
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1

            # Even length palindromes, centered at i and i+1
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
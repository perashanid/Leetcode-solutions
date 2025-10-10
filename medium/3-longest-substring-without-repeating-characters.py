"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(min(m, n)), where n is the length of the string s, and m is the size of the character set (e.g., 26 for English alphabets).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """

        # Use a sliding window approach with a set to keep track of characters in the current window.
        char_set = set()
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Maximum length of the substring found so far

        # Iterate through the string with the right pointer of the sliding window.
        for right in range(len(s)):
            # If the current character is already in the set, it means we have a repeating character.
            while s[right] in char_set:
                # Remove the leftmost character from the set and move the left pointer.
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set.
            char_set.add(s[right])

            # Update the maximum length with the current window size (right - left + 1).
            max_length = max(max_length, right - left + 1)

        return max_length
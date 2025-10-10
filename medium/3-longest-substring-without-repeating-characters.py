"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s. We iterate through the string at most twice.
# Space Complexity: O(min(m, n)), where n is the length of the string s and m is the size of the character set.
# In the worst case, the space is O(n) if all characters are unique. If the character set is limited (e.g., ASCII), it's O(1).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """

        # Initialize variables:
        # - start: The starting index of the current substring.
        # - max_length: The maximum length of a substring without repeating characters found so far.
        # - char_index_map: A dictionary to store the most recent index of each character.

        start = 0
        max_length = 0
        char_index_map = {}

        # Iterate through the string using a sliding window approach:
        for end in range(len(s)):
            # If the current character is already in the map and its index is within the current window:
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # Move the start of the window to the right of the previous occurrence of the character.
                start = char_index_map[s[end]] + 1

            # Update the index of the current character in the map.
            char_index_map[s[end]] = end

            # Update the maximum length.
            max_length = max(max_length, end - start + 1)

        # Return the maximum length.
        return max_length
"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-09
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(min(m, n)), where n is the length of the string s and m is the size of the character set (e.g., 26 for English alphabets, 128 for ASCII, 256 for extended ASCII).
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """

        # Initialize the start and end pointers of the sliding window.
        start = 0
        end = 0

        # Initialize the maximum length of the substring without repeating characters.
        max_length = 0

        # Initialize a set to store the characters in the current window.
        char_set = set()

        # Iterate over the string.
        while end < len(s):
            # If the current character is not in the set, add it to the set and update the maximum length.
            if s[end] not in char_set:
                char_set.add(s[end])
                max_length = max(max_length, end - start + 1)
                end += 1
            # If the current character is in the set, remove the character at the start of the window and move the start pointer forward.
            else:
                char_set.remove(s[start])
                start += 1

        # Return the maximum length.
        return max_length
"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(min(m, n)), where n is the length of the string s, and m is the size of the character set (e.g., 26 for lowercase English letters, 128 for ASCII, etc.).
# In the worst case, the entire string contains distinct characters, so the space complexity is O(n).
# If the character set is smaller than the length of the string, the space complexity is O(m).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """

        # Initialize a set to store the characters in the current substring.
        char_set = set()

        # Initialize the left pointer of the sliding window.
        left = 0

        # Initialize the maximum length of the substring found so far.
        max_length = 0

        # Iterate over the string using the right pointer of the sliding window.
        for right in range(len(s)):
            # While the current character is already in the set, remove the leftmost character from the set and move the left pointer.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set.
            char_set.add(s[right])

            # Update the maximum length.
            max_length = max(max_length, right - left + 1)

        # Return the maximum length.
        return max_length
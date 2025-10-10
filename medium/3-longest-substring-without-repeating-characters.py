"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(min(m, n)), where n is the length of the string s, and m is the size of the character set.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """

        # Create a set to store the characters in the current window.
        char_set = set()

        # Initialize the left and right pointers of the sliding window.
        left = 0
        right = 0

        # Initialize the maximum length of the substring without repeating characters.
        max_length = 0

        # Iterate over the string.
        while right < len(s):
            # If the current character is not in the set, add it to the set and move the right pointer.
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            # If the current character is in the set, remove the character at the left pointer from the set and move the left pointer.
            else:
                char_set.remove(s[left])
                left += 1

        # Return the maximum length.
        return max_length
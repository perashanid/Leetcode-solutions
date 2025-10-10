"""
Problem: Reverse Words in a String
Number: 151
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-words-in-a-string/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(n), where n is the length of the input string due to the list of words.

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses the order of words in a given string.

        Args:
            s (str): The input string containing words separated by spaces.

        Returns:
            str: The string with the words reversed and separated by a single space,
                 without leading or trailing spaces.
        """

        # 1. Split the string into a list of words, handling multiple spaces.
        words = s.split()

        # 2. Reverse the list of words.
        words.reverse()

        # 3. Join the reversed list of words with a single space.
        reversed_string = " ".join(words)

        # 4. Return the reversed string.
        return reversed_string
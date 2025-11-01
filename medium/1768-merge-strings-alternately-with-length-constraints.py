"""
Problem: Merge Strings Alternately with Length Constraints
Number: 1768
Difficulty: Medium
Link: https://leetcode.com/problems/merge-strings-alternately/
Date: 2025-11-01
"""

def merge_alternately(word1: str, word2: str) -> str:
    """
    Merges two strings by adding letters in an alternating fashion, starting with word1.
    If a string is longer than the other, append the additional letters onto the end of the merged string.

    Time Complexity: O(m+n), where m and n are the lengths of word1 and word2, respectively.
    Space Complexity: O(m+n), as the merged string can have a length of up to m+n.
    """

    merged = ""
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged += word1[i]
        merged += word2[j]
        i += 1
        j += 1

    # Append the remaining characters from word1, if any
    while i < len(word1):
        merged += word1[i]
        i += 1

    # Append the remaining characters from word2, if any
    while j < len(word2):
        merged += word2[j]
        j += 1

    return merged

# Example Usage/Test Cases
# print(merge_alternately("abc", "pqr"))  # Output: "apbqcr"
# print(merge_alternately("ab", "pqrs")) # Output: "apbqrs"
# print(merge_alternately("abcd", "pq")) # Output: "apbqcd"
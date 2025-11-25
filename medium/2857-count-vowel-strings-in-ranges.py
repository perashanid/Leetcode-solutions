"""
Problem: Count Vowel Strings in Ranges
Number: 2857
Difficulty: Medium
Link: https://leetcode.com/problems/count-vowel-strings-in-ranges/
Date: 2025-11-25
"""

# Time Complexity: O(n + m), where n is the number of words and m is the number of queries.
# Space Complexity: O(n), where n is the number of words (for the prefix sum array).

def vowel_strings(words, queries):
    """
    Counts the number of vowel strings in given ranges.

    Args:
        words: A list of strings.
        queries: A list of integer pairs representing start and end indices.

    Returns:
        A list of integers representing the number of vowel strings in each query range.
    """

    def is_vowel(char):
        """
        Checks if a character is a vowel.
        """
        return char in 'aeiou'

    def starts_and_ends_with_vowel(word):
        """
        Checks if a word starts and ends with a vowel.
        """
        return is_vowel(word[0]) and is_vowel(word[-1])

    # Create a prefix sum array to store the cumulative count of vowel strings.
    prefix_sum = [0] * (len(words) + 1)
    for i in range(len(words)):
        prefix_sum[i + 1] = prefix_sum[i] + (1 if starts_and_ends_with_vowel(words[i]) else 0)

    # Process each query and calculate the number of vowel strings in the range.
    result = []
    for start, end in queries:
        result.append(prefix_sum[end + 1] - prefix_sum[start])

    return result


# Example usage:
if __name__ == '__main__':
    words1 = ["aba", "bcb", "ece", "aa", "e"]
    queries1 = [[0, 2], [1, 4], [1, 1]]
    print(f"Example 1: words = {words1}, queries = {queries1}, result = {vowel_strings(words1, queries1)}")  # Output: [2, 3, 0]

    words2 = ["a", "e", "i"]
    queries2 = [[0, 2], [0, 1], [0, 0]]
    print(f"Example 2: words = {words2}, queries = {queries2}, result = {vowel_strings(words2, queries2)}")  # Output: [3, 2, 1]

    words3 = ["ab","abc","bc","b"]
    queries3 = [[0,0],[1,2],[2,3],[0,3]]
    print(f"Example 3: words = {words3}, queries = {queries3}, result = {vowel_strings(words3, queries3)}") # Output: [0, 0, 0, 0]
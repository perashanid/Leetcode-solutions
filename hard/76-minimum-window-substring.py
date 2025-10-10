"""
Problem: Minimum Window Substring
Number: 76
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/
Date: 2025-10-10
"""

# Time Complexity: O(S + T), where S is the length of string s and T is the length of string t.
# Space Complexity: O(T), where T is the number of distinct characters in string t.

def minWindow(s: str, t: str) -> str:
    """
    Finds the minimum window in string s which contains all characters in string t.

    Args:
        s (str): The string to search in.
        t (str): The string containing the characters to find.

    Returns:
        str: The minimum window in s containing all characters in t.
             Returns "" if no such window exists.
    """

    if not s or not t:
        return ""

    # Create a dictionary to store the frequency of characters in t.
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    # Initialize variables for the sliding window.
    required = len(dict_t)  # Number of distinct characters in t that need to be found in s.
    formed = 0  # Number of distinct characters in t that have been found in s with the required frequency.
    window_counts = {}  # Dictionary to store the frequency of characters in the current window.
    left = 0  # Left pointer of the sliding window.
    right = 0  # Right pointer of the sliding window.

    # Initialize variables to store the minimum window found so far.
    min_len = float('inf')
    start = 0
    end = 0

    # Iterate through the string s using the right pointer.
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If the character is in t and its frequency in the window matches its frequency in t, increment formed.
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        # While all characters in t have been found in the window, try to shrink the window from the left.
        while left <= right and formed == required:
            char = s[left]

            # Save the minimum window found so far.
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
                end = right

            # Remove the character at the left pointer from the window.
            window_counts[char] -= 1

            # If the character is in t and its frequency in the window is now less than its frequency in t, decrement formed.
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            # Move the left pointer to the right.
            left += 1

        # Move the right pointer to the right.
        right += 1

    # If no window was found, return "".
    if min_len == float('inf'):
        return ""

    # Return the minimum window found.
    return s[start:end + 1]
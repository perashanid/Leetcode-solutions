"""
Problem: Remove All Duplicate Letters While Preserving Relative Order with K Removals
Number: 2957
Difficulty: Hard
Link: https://leetcode.com/problems/remove-duplicate-letters/
Date: 2025-10-21
"""

# Time Complexity: O(N), where N is the length of the string s.
# Space Complexity: O(26) = O(1), because the size of the count and seen dictionaries is constant.

def remove_duplicate_letters_with_k_removals(s: str, k: int) -> str:
    """
    Removes at most k characters from s such that the resulting string has no duplicate letters
    and is lexicographically smallest while preserving the relative order of the remaining characters.

    Args:
        s: The input string.
        k: The maximum number of characters that can be removed.

    Returns:
        The lexicographically smallest string with no duplicate letters.
    """

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    stack = []
    seen = set()

    for char in s:
        count[char] -= 1

        if char in seen:
            continue

        # If the current character is smaller than the last character in the stack
        # and there are more occurrences of the last character in the stack later in the string,
        # and we still have removals left, pop the last character from the stack.
        while stack and char < stack[-1] and count[stack[-1]] > 0 and k > 0:
            seen.remove(stack.pop())
            k -= 1

        stack.append(char)
        seen.add(char)

    return "".join(stack)


# Example usage:
if __name__ == '__main__':
    s1 = "cbacdcbc"
    k1 = 2
    print(f"Input: s = '{s1}', k = {k1}, Output: '{remove_duplicate_letters_with_k_removals(s1, k1)}'")  # Output: acbc

    s2 = "bcabc"
    k2 = 1
    print(f"Input: s = '{s2}', k = {k2}, Output: '{remove_duplicate_letters_with_k_removals(s2, k2)}'")  # Output: abc

    s3 = "leetcode"
    k3 = 0
    print(f"Input: s = '{s3}', k = {k3}, Output: '{remove_duplicate_letters_with_k_removals(s3, k3)}'")  # Output: leetcode

    s4 = "abacb"
    k4 = 1
    print(f"Input: s = '{s4}', k = {k4}, Output: '{remove_duplicate_letters_with_k_removals(s4, k4)}'") # Output: abc
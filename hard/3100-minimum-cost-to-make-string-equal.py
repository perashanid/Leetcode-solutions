"""
Problem: Minimum Cost to Make String Equal
Number: 3100
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-make-two-strings-identical/
Date: 2025-10-22
"""

# Time Complexity: O(N^2)
# Space Complexity: O(N)
def min_cost_to_make_equal(s1: str, s2: str) -> int:
    """
    Calculates the minimum cost required to make s1 equal to s2 by swapping characters.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The minimum total cost required to make s1 equal to s2.
        Returns -1 if it is impossible to make s1 equal to s2.
    """

    n = len(s1)
    if len(s1) != len(s2):
        return -1

    counts = {}
    for char in s1:
        counts[char] = counts.get(char, 0) + 1
    for char in s2:
        counts[char] = counts.get(char, 0) - 1

    for count in counts.values():
        if count != 0:
            return -1

    diff_indices_s1 = []
    diff_indices_s2 = []

    for i in range(n):
        if s1[i] != s2[i]:
            diff_indices_s1.append(i)
    
    cost = 0
    while diff_indices_s1:
        i = diff_indices_s1.pop(0)
        
        # find index j in s2 such that s1[i] = s2[j] and s1[j] = s2[i]
        j = -1
        for k in range(len(diff_indices_s1)):
          index = diff_indices_s1[k]
          if s1[i] == s2[index] and s1[index] == s2[i]:
            j = index
            diff_indices_s1.pop(k)
            break

        if j != -1:
          cost += abs(i - j)
          continue

        #find an index j in s2 such that s1[i] == s2[j]
        j = -1
        for k in range(n):
          if s1[i] == s2[k] and s1[k] != s1[k]:
            j = k
            break

        if j == -1:
          #find an index j in diff indices s2 such that s1[i] == s2[j]
          j = -1
          for k in range(len(diff_indices_s1)):
            index = diff_indices_s1[k]
            if s1[i] == s2[index]:
              j = index
              diff_indices_s1.pop(k)
              break
        
        if j != -1:
          cost += abs(i - j)
          continue

    return cost

# Example usage
# s1 = "abca"
# s2 = "abac"
# print(min_cost_to_make_equal(s1, s2))  # Output: 1

# s1 = "abc"
# s2 = "cba"
# print(min_cost_to_make_equal(s1, s2))  # Output: 2

# s1 = "aab"
# s2 = "bbb"
# print(min_cost_to_make_equal(s1, s2))  # Output: -1
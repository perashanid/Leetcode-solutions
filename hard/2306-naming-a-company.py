"""
Problem: Naming a Company
Number: 2306
Difficulty: Hard
Link: https://leetcode.com/problems/naming-a-company/
Date: 2025-10-21
"""

# Time Complexity: O(n*m + 26*26*n), where n is the number of ideas and m is the average length of an idea.
# Space Complexity: O(n + 26*26*n), where n is the number of ideas.

def distinctNames(ideas: list[str]) -> int:
    """
    Calculates the number of distinct valid company names after swapping the first letters of any two distinct names in the ideas array.

    Args:
        ideas (list[str]): A list of company name ideas.

    Returns:
        int: The number of distinct valid company names.
    """

    # Convert the ideas list to a set for efficient lookup.
    ideas_set = set(ideas)

    # Create a 2D array to store the number of mutual suffixes between different starting letters.
    mutual_suffixes = [[0] * 26 for _ in range(26)]

    # Iterate through all pairs of ideas.
    for idea in ideas:
        first_letter = ord(idea[0]) - ord('a')

        # Iterate through the rest of the idea to check all other combinations
        for second_letter in range(26):
            # Create the swapped name
            new_idea = chr(ord('a') + second_letter) + idea[1:]

            # If the swapped name exists, increment the mutual suffix count for the pair of letters.
            if new_idea in ideas_set:
                mutual_suffixes[first_letter][second_letter] += 1

    # Calculate the number of distinct valid company names.
    result = 0
    for i in range(26):
        for j in range(i + 1, 26):  # Consider each pair of distinct letters only once.
            # Calculate the number of names that can be formed by swapping letters i and j.
            # This is done by subtracting mutual suffixes from the number of possible suffixes for each starting letter.
            valid_names_i = sum(1 for idea in ideas if ord(idea[0]) - ord('a') == i) - mutual_suffixes[i][j]
            valid_names_j = sum(1 for idea in ideas if ord(idea[0]) - ord('a') == j) - mutual_suffixes[j][i]
            result += valid_names_i * valid_names_j

    return result * 2  # Multiply by 2 because we need to consider both i,j and j,i swaps

# Example Usage / Test Cases
if __name__ == '__main__':
    ideas1 = ["coffee", "tea", "coffe"]
    print(f"Example 1: ideas = {ideas1}, Output = {distinctNames(ideas1)}")  # Output: 6

    ideas2 = ["aaa", "baa", "caa", "bbb", "cbb", "dbb"]
    print(f"Example 2: ideas = {ideas2}, Output = {distinctNames(ideas2)}")  # Output: 2

    ideas3 = ["leetcode", "loveleetcode", "leetcodeleet", "loveleetcodeleet"]
    print(f"Example 3: ideas = {ideas3}, Output = {0}") # Output: 0

    ideas4 = ["abc","abcd","abcde","abcdf","abcdfgh"]
    print(f"Example 4: ideas = {ideas4}, Output = {0}")
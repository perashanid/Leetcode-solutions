"""
Problem: Maximum Sum of Non-Adjacent Subtrees
Number: 4311
Difficulty: Hard
Link: https://leetcode.com/problems/house-robber-iii/
Date: 2025-10-25
"""

# Time Complexity: O(n), where n is the number of nodes in the tree.  We visit each node once during the DFS.
# Space Complexity: O(n), primarily due to the recursion stack and the storage for the `dp` table. In the worst-case scenario (a skewed tree), the recursion depth can be O(n).

def max_sum_non_adjacent_subtrees(n, adj, values):
    """
    Calculates the maximum sum of node values in a tree such that no two selected nodes are adjacent.

    Args:
        n (int): The number of nodes in the tree.
        adj (list of lists): An adjacency list representing the tree. adj[i] contains a list of neighbors of node i+1.
        values (list of int): An array of node values, where values[i] is the value of node i+1.

    Returns:
        int: The maximum sum of node values in a non-adjacent subset.
    """

    # dp[node][0] stores the max sum excluding the current node
    # dp[node][1] stores the max sum including the current node
    dp = {}

    def dfs(node, parent):
        """
        Performs a Depth-First Search (DFS) to calculate the maximum sum for each node.

        Args:
            node (int): The current node being visited.
            parent (int): The parent of the current node.
        """
        dp[node] = [0, values[node - 1]]  # Initialize dp values for the current node

        for neighbor in adj[node - 1]:
            if neighbor != parent:
                dfs(neighbor, node)
                # If we don't include the current node, we can choose to include or exclude its children
                dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
                # If we include the current node, we must exclude its children
                dp[node][1] += dp[neighbor][0]

    dfs(1, 0)  # Start DFS from node 1 (arbitrary root) with no parent
    return max(dp[1][0], dp[1][1])  # Return the maximum of including or excluding the root

# Example usage:
# n = 6
# adj = [
#     [2, 3, 4],
#     [1, 5, 6],
#     [1],
#     [1],
#     [2],
#     [2]
# ]
# values = [10, 1, 2, 3, 4, 5]
# print(max_sum_non_adjacent_subtrees(n, adj, values))  # Output: 19

# n = 4
# adj = [[2,3,4],[1],[1],[1]]
# values = [1,2,3,4]
# print(max_sum_non_adjacent_subtrees(n, adj, values)) #Output : 9
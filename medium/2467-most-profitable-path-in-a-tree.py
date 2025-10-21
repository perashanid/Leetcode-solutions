"""
Problem: Most Profitable Path in a Tree
Number: 2467
Difficulty: Medium
Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/
Date: 2025-10-21
"""

def mostProfitablePath(edges, amount, bob):
    """
    Finds the maximum revenue Bob can obtain if Alice starts at node bob.

    Time Complexity: O(N), where N is the number of nodes in the tree.
    Space Complexity: O(N), where N is the number of nodes in the tree.
    """

    n = len(amount)

    # 1. Build the adjacency list representation of the tree.
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # 2. Find Bob's path to the root (node 0) and the time it takes to reach each node.
    bob_path = [-1] * n
    def dfs_bob(node, parent, time):
        bob_path[node] = time
        for neighbor in adj[node]:
            if neighbor != parent:
                dfs_bob(neighbor, node, time + 1)
    dfs_bob(bob, -1, 0)

    # 3. Find the maximum revenue Alice can obtain from each leaf node.
    max_revenue = float('-inf')
    def dfs_alice(node, parent, revenue, time):
        nonlocal max_revenue

        # Calculate the revenue for the current node, considering Bob's path.
        if bob_path[node] == -1 or time < bob_path[node]:
            revenue += amount[node]
        elif time == bob_path[node]:
            revenue += amount[node] // 2  # Count the node's value only once
        # else: time > bob_path[node] -> Bob already visited

        is_leaf = True
        for neighbor in adj[node]:
            if neighbor != parent:
                is_leaf = False
                dfs_alice(neighbor, node, revenue, time + 1)

        if is_leaf:
            max_revenue = max(max_revenue, revenue)

    dfs_alice(0, -1, 0, 0)

    return max_revenue

if __name__ == '__main__':
    # Example 1
    edges1 = [[0, 1], [1, 2], [1, 3], [3, 4]]
    amount1 = [-2, 4, 2, -10, 6]
    bob1 = 3
    print(f"Example 1: {mostProfitablePath(edges1, amount1, bob1)}")  # Output: 17

    # Example 2
    edges2 = [[0, 1]]
    amount2 = [-7, 10]
    bob2 = 1
    print(f"Example 2: {mostProfitablePath(edges2, amount2, bob2)}")  # Output: 3

    # Example 3: A more complex test case
    edges3 = [[0, 2], [0, 3], [2, 4], [3, 5], [4, 6]]
    amount3 = [0, -100, 100, 50, 20, -30, 80]
    bob3 = 5
    print(f"Example 3: {mostProfitablePath(edges3, amount3, bob3)}") # Output: 230

    # Example 4: Bob starts at root
    edges4 = [[0, 1], [0, 2], [1, 3], [2, 4]]
    amount4 = [10, 20, 30, 40, 50]
    bob4 = 0
    print(f"Example 4: {mostProfitablePath(edges4, amount4, bob4)}") # Output: 150
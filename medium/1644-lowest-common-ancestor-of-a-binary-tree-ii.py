"""
Problem: Lowest Common Ancestor of a Binary Tree II
Number: 1644
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
Date: 2025-10-16
"""

# Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node at most once.
# Space Complexity: O(H), where H is the height of the tree. In the worst case (skewed tree), H = N. In the best case (balanced tree), H = logN.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor (LCA) of two nodes p and q in a binary tree.
        If either node p or q does not exist in the tree, return null.

        Args:
            root: The root of the binary tree.
            p: The first node.
            q: The second node.

        Returns:
            The lowest common ancestor of p and q, or null if either p or q is not in the tree.
        """

        p_exists = self.node_exists(root, p)
        q_exists = self.node_exists(root, q)

        if not p_exists or not q_exists:
            return None

        return self.lca_helper(root, p, q)

    def node_exists(self, root: TreeNode, target: TreeNode) -> bool:
        """
        Checks if a node exists in the tree.

        Args:
            root: The root of the subtree to search.
            target: The node to search for.

        Returns:
            True if the node exists in the tree, False otherwise.
        """
        if not root:
            return False

        if root == target:
            return True

        return self.node_exists(root.left, target) or self.node_exists(root.right, target)

    def lca_helper(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Helper function to recursively find the lowest common ancestor.

        Args:
            root: The root of the subtree to search.
            p: The first node.
            q: The second node.

        Returns:
            The lowest common ancestor of p and q in the subtree rooted at root.
        """
        if not root:
            return None

        if root == p or root == q:
            return root

        left_lca = self.lca_helper(root.left, p, q)
        right_lca = self.lca_helper(root.right, p, q)

        if left_lca and right_lca:
            return root
        elif left_lca:
            return left_lca
        else:
            return right_lca
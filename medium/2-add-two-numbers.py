"""
Problem: Add Two Numbers
Number: 2
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/
Date: 2025-10-10
"""

# Time Complexity: O(max(m, n)), where m and n are the lengths of the input lists.  We iterate at most once through both lists.
# Space Complexity: O(max(m, n) + 1), primarily due to the creation of the new linked list. In the worst case, the length of the result list is max(m, n) + 1.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two numbers represented as linked lists.

        Args:
            l1: The first linked list representing a non-negative integer.
            l2: The second linked list representing a non-negative integer.

        Returns:
            A new linked list representing the sum of the two input numbers.
        """

        carry = 0  # Initialize carry to 0
        dummy_head = ListNode(0)  # Create a dummy head node for the result list
        current = dummy_head  # Initialize a pointer to the current node in the result list

        # Iterate until both lists are exhausted
        while l1 or l2 or carry:
            # Get the values of the current nodes, if they exist. Otherwise, use 0.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry
            sum_val = val1 + val2 + carry

            # Update the carry for the next iteration
            carry = sum_val // 10

            # Calculate the digit to be added to the result list
            digit = sum_val % 10

            # Create a new node with the digit and add it to the result list
            current.next = ListNode(digit)

            # Move the current pointer to the next node
            current = current.next

            # Move to the next nodes in the input lists, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list (excluding the dummy head)
        return dummy_head.next
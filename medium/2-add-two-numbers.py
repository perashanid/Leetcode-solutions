"""
Problem: Add Two Numbers
Number: 2
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/
Date: 2025-10-10
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(max(m, n)), where m and n are the lengths of the linked lists.
    # Space Complexity: O(max(m, n)), for the length of the new list.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two numbers represented by linked lists and returns the sum as a linked list.

        Args:
            l1: The first linked list representing a number.
            l2: The second linked list representing a number.

        Returns:
            A linked list representing the sum of the two numbers.
        """

        dummy_head = ListNode(0)  # Dummy head to simplify the code
        current = dummy_head      # Pointer to the current node in the result list
        carry = 0                 # Carry-over from the previous addition

        # Iterate through the linked lists until both are exhausted
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry
            total = val1 + val2 + carry

            # Calculate the carry-over for the next digit
            carry = total // 10

            # Calculate the digit for the current node
            digit = total % 10

            # Create a new node with the digit and append it to the result list
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in the input lists, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list, skipping the dummy head
        return dummy_head.next
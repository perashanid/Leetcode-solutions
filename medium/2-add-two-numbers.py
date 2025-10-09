"""
Problem: Add Two Numbers
Number: 2
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/
Date: 2025-10-09
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.

    Time Complexity: O(max(m, n)), where m and n are the lengths of the two linked lists.
    Space Complexity: O(max(m, n)), for the length of the new list.

    Args:
        l1 (ListNode): The first linked list.
        l2 (ListNode): The second linked list.

    Returns:
        ListNode: The sum as a linked list.
    """

    carry = 0
    dummy_head = ListNode(0)  # Create a dummy head node for the result list
    current = dummy_head

    while l1 or l2 or carry:
        # Get the values of the current nodes (or 0 if the list is empty)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum of the current digits and the carry
        sum_val = val1 + val2 + carry

        # Calculate the new carry and the digit to add to the result list
        carry = sum_val // 10
        digit = sum_val % 10

        # Create a new node with the digit and add it to the result list
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes in the input lists (if they exist)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Return the result list (excluding the dummy head)
    return dummy_head.next
"""
Problem: Sort List
Number: 148
Difficulty: Medium
Link: https://leetcode.com/problems/sort-list/
Date: 2025-10-12
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(n log n) - due to merge sort
# Space Complexity: O(1) - in-place merge sort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sorts a linked list in O(n log n) time using constant space complexity (merge sort).

        Args:
            head: The head of the linked list.

        Returns:
            The head of the sorted linked list.
        """

        if not head or not head.next:
            return head  # Base case: empty or single-node list is already sorted

        # 1. Split the list into two halves
        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None  # Disconnect the two halves

        # 2. Recursively sort the two halves
        left = self.sortList(left)
        right = self.sortList(right)

        # 3. Merge the sorted halves
        return self.merge(left, right)

    def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a linked list using the slow and fast pointer approach.

        Args:
            head: The head of the linked list.

        Returns:
            The middle node of the linked list.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a single sorted linked list.

        Args:
            list1: The head of the first sorted linked list.
            list2: The head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.
        """

        dummy = ListNode()  # Dummy node to simplify merging
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append any remaining nodes from either list
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next  # Return the head of the merged list (excluding the dummy node)
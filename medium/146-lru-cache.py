"""
Problem: LRU Cache
Number: 146
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/
Date: 2025-10-12
"""

# Time Complexity: O(1) for both get and put operations
# Space Complexity: O(capacity), where capacity is the maximum number of items in the cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key-node pairs for O(1) access
        self.left = Node(0, 0)  # Dummy head node
        self.right = Node(0, 0)  # Dummy tail node
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        """Removes a node from the doubly linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        """Inserts a node at the right end (most recently used) of the doubly linked list."""
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        """
        Returns the value of the key if the key exists in the cache, otherwise returns -1.
        Moves the accessed node to the right end (most recently used).
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Updates the value of the key if the key exists.
        Otherwise, adds the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evicts the least recently used key.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            # Evict the least recently used node (left.next)
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
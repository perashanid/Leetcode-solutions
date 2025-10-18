"""
Problem: LFU Cache
Number: 460
Difficulty: Hard
Link: https://leetcode.com/problems/lfu-cache/
Date: 2025-10-18
"""

# Time Complexity: O(1) for both get and put operations
# Space Complexity: O(capacity)
from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        """
        Initializes the LFU Cache with a given capacity.

        Args:
            capacity (int): The maximum number of key-value pairs the cache can hold.
        """
        self.capacity = capacity
        self.key_to_val = {}  # Stores key-value pairs
        self.key_to_freq = {}  # Stores key-frequency pairs
        self.freq_to_keys = defaultdict(list)  # Stores frequency-keys mapping
        self.min_freq = 1  # Keeps track of the minimum frequency in the cache

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with a given key.
        If the key is not present, returns -1.
        Updates the frequency of the key if found.

        Args:
            key (int): The key to retrieve.

        Returns:
            int: The value associated with the key, or -1 if the key is not present.
        """
        if key not in self.key_to_val:
            return -1

        freq = self.key_to_freq[key]

        # Remove the key from the current frequency list
        self.freq_to_keys[freq].remove(key)
        if not self.freq_to_keys[freq]:  # If the frequency list is empty, remove it.
            if self.min_freq == freq: # If it's the minimum freq, increase min_freq
                self.min_freq += 1
            del self.freq_to_keys[freq]

        # Increment the frequency and add the key to the new frequency list
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1].append(key)

        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair in the cache.
        If the cache is at capacity, evicts the least frequently used key.
        Resets the frequency to 1 for new keys.

        Args:
            key (int): The key to insert or update.
            value (int): The value to associate with the key.
        """
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Update the value if the key already exists
            self.key_to_val[key] = value
            self.get(key) # Update frequency

        else:
            # Evict the least frequently used key if the cache is full
            if len(self.key_to_val) == self.capacity:
                # Find the least frequently used key (from min_freq)
                evict_key = self.freq_to_keys[self.min_freq].pop(0)

                if not self.freq_to_keys[self.min_freq]:  # Remove if list is empty
                    del self.freq_to_keys[self.min_freq]
                
                del self.key_to_val[evict_key]
                del self.key_to_freq[evict_key]
            
            # Insert the new key-value pair
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1].append(key)
            self.min_freq = 1  # Reset min_freq to 1 for new keys
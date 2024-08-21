#!/usr/bin/env python3
"""LRU cache"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain order of access

    def put(self, key, item):
        if key is None or item is None:
            return

        # Add or update the item in the cache
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Move the key to the end to mark it as recently used
        self.cache_data[key] = item

        # Check if we need to discard the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)  # Remove the oldest item
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

#!/usr/bin/python3
"""LRU cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching a caching system using LRU algorithm"""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key from the cache"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None

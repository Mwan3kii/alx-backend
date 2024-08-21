#!/usr/bin/python3
"""MRU caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache inherits from BaseCaching and is a caching system using MRU algorithm."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """Get an item by key from the cache"""
        if key in self.cache_data:
            self.last_key = key
            return self.cache_data[key]
        return None

#!/usr/bin/python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is caching system without limit"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the cache"""
        return self.cache_data.get(key, None)

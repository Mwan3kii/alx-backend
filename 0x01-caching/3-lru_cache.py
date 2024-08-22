#!/usr/bin/env python3
"""LRU cache implementation"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching a caching system using MRU algorithm"""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item in the cache
        Args:
            key: The key associated with the item to cache.
            item: The item to cache.

        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Get item by key from the cache

        Args:
            key: The key associated with the item to retrieve.
        Returns:
            The cached item or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

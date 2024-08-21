#!/usr/bin/python3
"""LFU cacnhing"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """Inherits from BaseCaching caching system using LFU algorithm."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.freq = defaultdict(int)
        self.use_order = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.freq[key] += 1
                self.use_order.move_to_end(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_freq = min(self.freq.values())
                    lfu_keys = [
                        k for k, v in self.freq.items() if v == min_freq
                    ]
                    if len(lfu_keys) == 1:
                        key_to_discard = lfu_keys[0]
                    else:
                        for k in self.use_order:
                            if k in lfu_keys:
                                key_to_discard = k
                                break
                    del self.cache_data[key_to_discard]
                    del self.freq[key_to_discard]
                    del self.use_order[key_to_discard]
                    print(f"DISCARD: {key_to_discard}")
                self.cache_data[key] = item
                self.freq[key] = 1
                self.use_order[key] = None

    def get(self, key):
        """Get an item by key from the cache"""
        if key in self.cache_data:
            self.freq[key] += 1
            self.use_order.move_to_end(key)
            return self.cache_data[key]
        return None

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching and is a caching system using LRU algorithm."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache.
        
        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the order list to reflect the recent use of the key
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, remove the least recently used item (LRU)
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new item and update the order list
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key from the cache.
        
        Args:
            key: The key of the item to be retrieved.
        
        Returns:
            The item if the key exists in the cache, otherwise None.
        """
        if key in self.cache_data:
            # Update the order list to reflect the recent use of the key
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
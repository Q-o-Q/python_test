from collections import OrderedDict


class LRUCache:
    """
    LRU (Least Recently Used) 缓存实现

    使用 OrderedDict 实现，保持 O(1) 的访问和插入时间复杂度
    """

    def __init__(self, capacity: int):
        """
        初始化 LRU 缓存

        :param capacity: 缓存容量
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: any) -> any:
        """
        Retrieves the value associated with the given key from the cache.
        
        Returns:
            The value if the key exists in the cache; otherwise, None.
        """
        if key not in self.cache:
            return None
        return self.cache[key]

    def put(self, key: any, value: any) -> None:
        """
        Inserts or updates a key-value pair in the cache, evicting the least recently used item if necessary.
        
        If the key already exists, it is marked as recently used. If the cache is at capacity and the key is new, the least recently used item is removed before insertion.
        """
        if key in self.cache:
            # 如果键已存在，更新值并移到末尾
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # 如果缓存已满，弹出最久未使用的元素（字典头部）
                self.cache.popitem(last=False)

    def __len__(self) -> int:
        """
        Returns the number of items currently stored in the cache.
        """
        return len(self.cache)

    def clear(self) -> None:
        """清空缓存"""
        self.cache.clear()

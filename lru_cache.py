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
        获取键对应的值

        :param key: 要查找的键
        :return: 如果键存在返回对应的值，否则返回 None
        """
        if key not in self.cache:
            return None

        # 将访问的键移到字典末尾表示最近使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: any, value: any) -> None:
        """
        插入键值对到缓存中

        :param key: 要插入的键
        :param value: 要插入的值
        """
        if key in self.cache:
            # 如果键已存在，更新值并移到末尾
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # 如果缓存已满，弹出最久未使用的元素（字典头部）
                self.cache.popitem(last=False)

        # 插入或更新键值对
        self.cache[key] = value

    def __len__(self) -> int:
        """返回当前缓存中的元素数量"""
        return len(self.cache)

    def clear(self) -> None:
        """清空缓存"""
        self.cache.clear()

from collections import defaultdict, OrderedDict


class LFUCache:
    """
    LFU (Least Frequently Used) 缓存实现

    使用双层数据结构：
    - 外层：频率到键值的有序字典（OrderedDict）
    - 内层：键到值和频率的映射
    """

    def __init__(self, capacity: int):
        """
        初始化LFU缓存

        :param capacity: 缓存容量
        """
        self.capacity = capacity
        self.min_freq = 0  # 当前最小频率
        self.key_to_val_freq = {}  # 键到(值,频率)的映射
        self.freq_to_keys = defaultdict(OrderedDict)  # 频率到键的有序字典

    def get(self, key: any) -> any:
        """
        获取键对应的值

        :param key: 要查找的键
        :return: 如果键存在返回对应的值，否则返回None
        """
        if key not in self.key_to_val_freq:
            return None

        val, freq = self.key_to_val_freq[key]
        # 更新频率
        self._update_freq(key, val, freq)
        return val

    def put(self, key: any, value: any) -> None:
        """
        插入键值对到缓存中

        :param key: 要插入的键
        :param value: 要插入的值
        """
        if self.capacity <= 0:
            return

        if key in self.key_to_val_freq:
            # 键已存在，更新值并增加频率
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._update_freq(key, value, freq)
            return

        # 如果缓存已满，删除最少使用的项
        if len(self.key_to_val_freq) >= self.capacity:
            self._evict()

        # 插入新键值对，初始频率为1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def _update_freq(self, key: any, val: any, freq: int) -> None:
        """
        更新键的频率

        :param key: 要更新的键
        :param val: 对应的值
        :param freq: 当前频率
        """
        # 从原频率中删除
        del self.freq_to_keys[freq][key]

        # 如果原频率是最小频率且没有其他键了，更新最小频率
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1

        # 增加频率并添加到新频率的有序字典
        new_freq = freq + 1
        self.key_to_val_freq[key] = (val, new_freq)
        self.freq_to_keys[new_freq][key] = None

    def _evict(self) -> None:
        """
        淘汰最少使用的项
        """
        # 获取最小频率的第一个键（最久未使用）
        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        del self.key_to_val_freq[key]

    def __len__(self) -> int:
        """返回当前缓存中的元素数量"""
        return len(self.key_to_val_freq)

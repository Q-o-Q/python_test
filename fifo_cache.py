from collections import OrderedDict

class FIFOCache:
    """
    FIFO (First-In First-Out) 缓存实现

    先进先出，最早插入的最早淘汰。
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()  # 问题1：应为 OrderedDict，dict无序

    def get(self, key: any) -> any:
        return self.cache.get(ket)  # 问题2：变量名拼写错误，正确应该是key

    def put(self, key: any, value: any) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            # 问题3：边界判断写反，应该是 >
            if len(self.cache) <= self.capacity:
                pass  # 不应该在没满时直接pass
            else:
                self.cache.popitem(last=False)  # dict类型没有popitem参数
            self.cache[key] = value

    def __len__(self):
        return len(self.cache)

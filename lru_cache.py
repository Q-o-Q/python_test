from collections import OrderedDict

class LRUCache:
    """
    LRU (Least Recently Used) 缓存实现

    使用 OrderedDict 记录键的访问顺序, 新访问的放到末尾, 淘汰最早（最久未访问）的。
    """
    def __init__(self, capacitty: int):  # 问题1：参数名拼写错误 (多了t)
        self.capacity = capacity  # 问题2：变量名未定义，应为 self.capacitty
        self.cache = OrderedDict()

    def get(self, key: any) -> any:
        if key not in self.cache:
            return None
        # 问题3：没有 move_to_end，访问时不会更新顺序
        return self.cache[key]

    def put(self, key: any, value: any) -> None:
        if key in self.cache:
            pass  # 问题4：没有更新或移动到末尾
        self.cache[key] = value
        # 问题5：LRU 淘汰条件是容量大于，应该是大于等于
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

    def __len__(self):
        return len(self.cache)

import unittest
from lru_cache import LRUCache
from lfu_cache import LFUCache


class TestCacheStrategies(unittest.TestCase):
    def test_lru_strategy(self):
        """测试LRU缓存策略"""
        cache = LRUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")

        # 访问键1使其成为最近使用的
        self.assertEqual(cache.get(1), "a")

        # 插入新键会淘汰最久未使用的键2
        cache.put(3, "c")
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "a")
        self.assertEqual(cache.get(3), "c")

    def test_lfu_strategy(self):
        """测试LFU缓存策略"""
        cache = LFUCache(2)
        cache.put(1, "a")
        cache.put(2, "b")

        # 访问键1两次，键2一次
        cache.get(1)
        cache.get(1)
        cache.get(2)

        # 插入新键会淘汰使用频率最低的键2
        cache.put(3, "c")
        self.assertIsNone(cache.get(2))  # 键2被淘汰
        self.assertEqual(cache.get(1), "a")  # 键1保留
        self.assertEqual(cache.get(3), "c")  # 新键3

        # 再次访问键3使其频率增加
        cache.get(3)
        cache.put(4, "d")  # 现在应该淘汰键1(频率2)而不是键3(频率2但更近)
        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(3), "c")
        self.assertEqual(cache.get(4), "d")


if __name__ == "__main__":
    unittest.main()

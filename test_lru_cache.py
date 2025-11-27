import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_basic_operations(self):
        """测试基本操作"""
        cache = LRUCache(2)

        # 测试插入和获取
        cache.put(1, "a")
        cache.put(2, "b")
        self.assertEqual(cache.get(1), "a")

        # 测试超出容量时的淘汰策略
        cache.put(3, "c")  # 应该淘汰键2
        self.assertIsNone(cache.get(2))
        self.assertEqual(cache.get(1), "a")
        self.assertEqual(cache.get(3), "c")

        # 测试更新已有键
        cache.put(2, "x")
        self.assertEqual(cache.get(1), "x")

        # 测试长度
        self.assertEqual(len(cache), 2)

        # 测试清空
        cache.clear()
        self.assertEqual(len(cache), 0)


if __name__ == "__main__":
    unittest.main()

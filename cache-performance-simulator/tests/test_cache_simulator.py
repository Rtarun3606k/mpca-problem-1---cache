import unittest
from src.cache.cache_simulator import CacheSimulator

class TestCacheSimulator(unittest.TestCase):
    def setUp(self):
        self.cache = CacheSimulator(cache_size=16, block_size=4)

    def test_initial_conditions(self):
        self.assertEqual(self.cache.total_accesses, 0)
        self.assertEqual(self.cache.hits, 0)
        self.assertEqual(self.cache.misses, 0)

    def test_access_memory_hit(self):
        self.cache.access_memory(1000)  # Miss
        self.cache.access_memory(1000)  # Hit
        self.assertEqual(self.cache.hits, 1)
        self.assertEqual(self.cache.misses, 1)

    def test_access_memory_miss(self):
        self.cache.access_memory(1000)  # Miss
        self.cache.access_memory(2000)  # Miss
        self.assertEqual(self.cache.hits, 0)
        self.assertEqual(self.cache.misses, 2)

    def test_hit_rate(self):
        self.cache.access_memory(1000)  # Miss
        self.cache.access_memory(1000)  # Hit
        self.cache.access_memory(2000)  # Miss
        self.assertAlmostEqual(self.cache.get_hit_rate(), 33.33, places=2)

    def test_miss_rate(self):
        self.cache.access_memory(1000)  # Miss
        self.cache.access_memory(1000)  # Hit
        self.cache.access_memory(2000)  # Miss
        self.assertAlmostEqual(self.cache.get_miss_rate(), 66.67, places=2)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.cache.cache_simulator import CacheSimulator
from src.optimization.optimizer import Optimizer
from src.memory.trace_loader import load_memory_trace

class TestOptimizer(unittest.TestCase):
    def setUp(self):
        self.cache = CacheSimulator(cache_size=16, block_size=4)
        self.optimizer = Optimizer(self.cache)
        self.memory_trace = load_memory_trace('data/traces/sample_trace.txt')

    def test_optimizer_performance_improvement(self):
        # Simulate memory accesses before optimization
        for address in self.memory_trace:
            self.cache.access_memory(address)

        initial_hits = self.cache.hits
        initial_misses = self.cache.misses

        # Apply optimization strategies
        self.optimizer.apply_optimization()

        # Simulate memory accesses after optimization
        for address in self.memory_trace:
            self.cache.access_memory(address)

        improved_hits = self.cache.hits
        improved_misses = self.cache.misses

        # Check if hits have increased and misses have decreased
        self.assertGreater(improved_hits, initial_hits)
        self.assertLess(improved_misses, initial_misses)

    def test_optimizer_strategy_effectiveness(self):
        # Test specific optimization strategies
        original_hit_rate = self.cache.get_hit_rate()
        self.optimizer.apply_specific_strategy('some_strategy')  # Replace with actual strategy name

        # Simulate memory accesses after applying the strategy
        for address in self.memory_trace:
            self.cache.access_memory(address)

        new_hit_rate = self.cache.get_hit_rate()

        # Check if the hit rate has improved
        self.assertGreater(new_hit_rate, original_hit_rate)

if __name__ == '__main__':
    unittest.main()
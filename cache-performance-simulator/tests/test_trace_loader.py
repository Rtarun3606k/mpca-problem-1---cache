import unittest
from src.memory.trace_loader import load_memory_trace

class TestTraceLoader(unittest.TestCase):
    def test_load_memory_trace(self):
        # Test loading a valid memory trace file
        trace_file = 'data/traces/sample_trace.txt'
        expected_addresses = [1000, 1004, 2000, 1000, 3000, 1004, 4000]
        loaded_addresses = load_memory_trace(trace_file)
        self.assertEqual(loaded_addresses, expected_addresses)

    def test_load_non_existent_trace_file(self):
        # Test loading a non-existent memory trace file
        trace_file = 'data/traces/non_existent_trace.txt'
        with self.assertRaises(FileNotFoundError):
            load_memory_trace(trace_file)

    def test_load_empty_trace_file(self):
        # Test loading an empty memory trace file
        trace_file = 'data/traces/empty_trace.txt'
        with open(trace_file, 'w') as f:
            pass  # Create an empty file
        loaded_addresses = load_memory_trace(trace_file)
        self.assertEqual(loaded_addresses, [])

if __name__ == '__main__':
    unittest.main()
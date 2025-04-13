from cache.cache_simulator import CacheSimulator
from memory.trace_loader import load_memory_trace
from optimization.optimizer import Optimizer
from optimization.strategies import BlockSizeOptimizationStrategy, CacheSizeOptimizationStrategy
from visualization.stats_display import display_stats, compare_stats
import os

def generate_sample_trace(filename, with_locality=True):
    """Generate a sample trace file with memory access patterns"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    addresses = []
    
    # Generate addresses with spatial and temporal locality
    base_addresses = [1000, 5000, 10000, 15000]
    
    if with_locality:
        # With locality: access adjacent addresses and repeat access patterns
        for base in base_addresses:
            # Spatial locality: access consecutive addresses
            for i in range(5):
                addresses.append(base + i*4)  # Access consecutive words
            
            # Temporal locality: revisit some addresses
            addresses.append(base)
            addresses.append(base + 4)
            
        # Add some random accesses to mix it up
        addresses.extend([3000, 7000, 12000, 8000])
    else:
        # Without locality: just random accesses
        addresses = [1000, 5000, 9000, 13000, 17000, 2000, 6000, 10000, 14000, 18000,
                    3000, 7000, 11000, 15000, 19000, 4000, 8000, 12000, 16000, 20000]
    
    # Write to file
    with open(filename, 'w') as f:
        for addr in addresses:
            f.write(f"{addr}\n")
    
    return addresses

def main():
    """
    Main function to run the cache performance simulation
    """
    # Define trace file path
    trace_file = os.path.join("data", "traces", "sample_trace.txt")
    
    # Load memory trace
    addresses = load_memory_trace(trace_file)
    
    if not addresses:
        print("No addresses loaded. Using default test addresses with locality patterns.")
        # Addresses with spatial and temporal locality
        addresses = [
            1000, 1004, 1008, 1012, 1016,  # Spatial locality
            1000, 1004,                    # Temporal locality
            2000, 2004, 2008, 2012,        # Another region (spatial)
            2000, 2008,                    # Revisit (temporal)
            3000, 3004, 3008,              # New region
            1004, 2004                     # Revisit previous addresses
        ]
    
    print(f"Processing {len(addresses)} memory accesses...")
    
    # Original cache (direct-mapped, smaller blocks)
    original_cache = CacheSimulator(cache_size=16, block_size=4)
    for address in addresses:
        original_cache.access_memory(address)
    
    print("\nCache Statistics Before Optimization:")
    display_stats(original_cache)
    
    # Create optimized cache with larger block size and more lines
    optimized_cache = CacheSimulator(cache_size=32, block_size=16)
    for address in addresses:
        optimized_cache.access_memory(address)
    
    print("\nCache Statistics After Optimization:")
    display_stats(optimized_cache)
    
    # Compare results
    compare_stats(original_cache, optimized_cache, "Cache Parameter Optimization")

if __name__ == "__main__":
    main()
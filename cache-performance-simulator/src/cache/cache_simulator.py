class CacheSimulator:
    """
    A direct-mapped cache simulator that tracks hits and misses.
    Similar to the assembly implementation in cache_simulator.s
    """
    def __init__(self, cache_size=16, block_size=4):
        """
        Initialize the cache simulator.
        
        Args:
            cache_size (int): Number of cache lines
            block_size (int): Size of each block in bytes
        """
        self.cache_size = cache_size
        self.block_size = block_size
        
        # Add this line to fix the error - for a direct-mapped cache,
        # the number of sets equals the number of cache lines
        self.num_sets = cache_size
        
        # Initialize cache data structures
        self.tags = [0] * cache_size
        self.valid_bits = [0] * cache_size
        
        # Initialize counters
        self.total_accesses = 0
        self.hits = 0
        self.misses = 0
    
    def calculate_index_and_tag(self, address):
        """
        Calculate the set index and tag for a given memory address
        
        Args:
            address (int): Memory address
            
        Returns:
            tuple: (set_index, tag)
        """
        # Calculate index and tag based on block size and cache organization
        # For a cache with block_size bytes per block:
        # Block offset bits = log2(block_size) [not used directly here]
        # Set index bits = log2(num_sets)
        
        # Calculate set index: (address / block_size) % num_sets
        # This correctly accounts for different block sizes
        set_index = (address // self.block_size) % self.num_sets
        
        # Calculate tag: address / (block_size * num_sets)
        tag = address // (self.block_size * self.num_sets)
        
        return set_index, tag
    
    def access_memory(self, address):
        """
        Simulate a memory access at the given address.
        
        Args:
            address (int): Memory address to access
            
        Returns:
            bool: True for hit, False for miss
        """
        self.total_accesses += 1
        
        # Calculate index and tag for this address
        index, tag = self.calculate_index_and_tag(address)
        
        # Check if it's a hit
        if self.valid_bits[index] and self.tags[index] == tag:
            self.hits += 1
            return True
        else:
            # It's a miss, update cache
            self.misses += 1
            self.valid_bits[index] = 1
            self.tags[index] = tag
            return False
    
    def get_hit_rate(self):
        """
        Calculate the hit rate.
        
        Returns:
            float: Hit rate as a percentage
        """
        if self.total_accesses == 0:
            return 0.0
        
        return (self.hits / self.total_accesses) * 100.0
    
    def get_miss_rate(self):
        """
        Calculate the miss rate.
        
        Returns:
            float: Miss rate as a percentage
        """
        if self.total_accesses == 0:
            return 0.0
        
        return (self.misses / self.total_accesses) * 100.0
    
    def print_stats(self):
        """
        Print cache statistics.
        """
        print(f"Total memory accesses: {self.total_accesses}")
        print(f"Cache hits: {self.hits}")
        print(f"Cache misses: {self.misses}")
        print(f"Hit rate: {self.get_hit_rate():.2f}%")
        print(f"Miss rate: {self.get_miss_rate():.2f}%")
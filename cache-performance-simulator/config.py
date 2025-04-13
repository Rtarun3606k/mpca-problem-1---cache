class Config:
    """
    Configuration settings for the cache performance simulator.
    """
    CACHE_SIZE = 16  # Number of cache lines
    BLOCK_SIZE = 4   # Size of each block in bytes
    TRACE_FILE_PATH = 'data/traces/sample_trace.txt'  # Path to the memory trace file
    RESULTS_DIR = 'data/results'  # Directory to store results
    OPTIMIZATION_STRATEGY = 'default'  # Default optimization strategy to use

    @staticmethod
    def display_config():
        """
        Display the current configuration settings.
        """
        print("Cache Performance Simulator Configuration:")
        print(f"Cache Size: {Config.CACHE_SIZE}")
        print(f"Block Size: {Config.BLOCK_SIZE}")
        print(f"Trace File Path: {Config.TRACE_FILE_PATH}")
        print(f"Results Directory: {Config.RESULTS_DIR}")
        print(f"Optimization Strategy: {Config.OPTIMIZATION_STRATEGY}")
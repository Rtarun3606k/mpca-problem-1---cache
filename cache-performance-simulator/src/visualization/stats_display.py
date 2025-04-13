def display_cache_stats(cache_simulator, title="Cache Statistics"):
    """
    Display cache statistics including hits, misses, hit rate, and miss rate.

    Args:
        cache_simulator (CacheSimulator): An instance of the CacheSimulator class.
        title (str): Title for the statistics display.
    """
    print(f"{title}:")
    print(f"Total memory accesses: {cache_simulator.total_accesses}")
    print(f"Cache hits: {cache_simulator.hits}")
    print(f"Cache misses: {cache_simulator.misses}")
    print(f"Hit rate: {cache_simulator.get_hit_rate():.2f}%")
    print(f"Miss rate: {cache_simulator.get_miss_rate():.2f}%")


def display_optimized_stats(original_cache, optimized_cache):
    """
    Display cache statistics before and after optimization.

    Args:
        original_cache (CacheSimulator): The original cache simulator instance.
        optimized_cache (CacheSimulator): The optimized cache simulator instance.
    """
    print("Before Optimization:")
    display_cache_stats(original_cache, title="Original Cache Statistics")
    
    print("\nAfter Optimization:")
    display_cache_stats(optimized_cache, title="Optimized Cache Statistics")

def display_stats(cache_stats, title="Cache Statistics"):
    """
    Display cache statistics in a readable format.
    
    Args:
        cache_stats (dict or CacheSimulator): Dictionary containing cache statistics or CacheSimulator object
        title (str): Title for the statistics display
    """
    print(f"\n=== {title} ===")
    
    # Check if we received a CacheSimulator object instead of a dictionary
    if hasattr(cache_stats, 'total_accesses'):
        # It's a CacheSimulator object, extract the stats
        print(f"Total memory accesses: {cache_stats.total_accesses}")
        print(f"Cache hits: {cache_stats.hits}")
        print(f"Cache misses: {cache_stats.misses}")
        print(f"Hit rate: {cache_stats.get_hit_rate():.2f}%")
        print(f"Miss rate: {cache_stats.get_miss_rate():.2f}%")
    else:
        # It's a dictionary
        print(f"Total memory accesses: {cache_stats.get('total_accesses', 0)}")
        print(f"Cache hits: {cache_stats.get('hits', 0)}")
        print(f"Cache misses: {cache_stats.get('misses', 0)}")
        print(f"Hit rate: {cache_stats.get('hit_rate', 0.0):.2f}%")
        print(f"Miss rate: {cache_stats.get('miss_rate', 0.0):.2f}%")
        
        # If there are additional statistics, display them too
        for key, value in cache_stats.items():
            if key not in ['total_accesses', 'hits', 'misses', 'hit_rate', 'miss_rate']:
                if isinstance(value, float):
                    print(f"{key}: {value:.2f}")
                else:
                    print(f"{key}: {value}")
    print()

def compare_stats(before_stats, after_stats, optimization_name="Optimization"):
    """
    Compare and display statistics before and after optimization.
    
    Args:
        before_stats (dict or CacheSimulator): Statistics before optimization
        after_stats (dict or CacheSimulator): Statistics after optimization
        optimization_name (str): Name of the optimization strategy
    """
    print(f"\n=== {optimization_name} Comparison ===")
    
    # Extract hit rates based on the type of input
    if hasattr(before_stats, 'get_hit_rate'):
        hit_rate_before = before_stats.get_hit_rate()
        miss_rate_before = before_stats.get_miss_rate()
    else:
        hit_rate_before = before_stats.get('hit_rate', 0.0)
        miss_rate_before = before_stats.get('miss_rate', 0.0)
        
    if hasattr(after_stats, 'get_hit_rate'):
        hit_rate_after = after_stats.get_hit_rate()
        miss_rate_after = after_stats.get_miss_rate()
    else:
        hit_rate_after = after_stats.get('hit_rate', 0.0)
        miss_rate_after = after_stats.get('miss_rate', 0.0)
    
    # Calculate improvements
    hit_rate_improvement = hit_rate_after - hit_rate_before
    miss_rate_reduction = miss_rate_before - miss_rate_after
    
    # Display improvements
    print(f"Hit rate before: {hit_rate_before:.2f}%")
    print(f"Hit rate after: {hit_rate_after:.2f}%")
    print(f"Hit rate improvement: {hit_rate_improvement:.2f}% ({'+' if hit_rate_improvement > 0 else ''}{hit_rate_improvement:.2f}%)")
    
    print(f"Miss rate before: {miss_rate_before:.2f}%")
    print(f"Miss rate after: {miss_rate_after:.2f}%")
    print(f"Miss rate reduction: {miss_rate_reduction:.2f}% ({'+' if miss_rate_reduction > 0 else ''}{miss_rate_reduction:.2f}%)")
    
    # Check for avg_access_time
    has_access_time = False
    time_before = time_after = 0
    
    if hasattr(before_stats, 'avg_access_time'):
        time_before = before_stats.avg_access_time
        has_access_time = True
    elif isinstance(before_stats, dict) and 'avg_access_time' in before_stats:
        time_before = before_stats['avg_access_time']
        has_access_time = True
    
    if hasattr(after_stats, 'avg_access_time'):
        time_after = after_stats.avg_access_time
        has_access_time = True
    elif isinstance(after_stats, dict) and 'avg_access_time' in after_stats:
        time_after = after_stats['avg_access_time']
        has_access_time = True
    
    if has_access_time:
        time_improvement = time_before - time_after
        print(f"Average access time before: {time_before:.2f} ns")
        print(f"Average access time after: {time_after:.2f} ns")
        print(f"Access time reduction: {time_improvement:.2f} ns ({(time_improvement/time_before*100) if time_before > 0 else 0:.2f}%)")
    
    print()
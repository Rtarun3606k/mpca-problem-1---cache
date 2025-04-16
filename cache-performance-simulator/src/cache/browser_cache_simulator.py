from collections import OrderedDict
import matplotlib.pyplot as plt

class BrowserLRUCache:
    """
    A browser cache simulator that implements the LRU (Least Recently Used) caching policy.
    This simulates a browser cache that stores the last N visited web pages.
    """
    def __init__(self, capacity):
        """
        Initialize the browser cache simulator.
        
        Args:
            capacity (int): Maximum number of pages that can be stored in the cache
        """
        self.capacity = capacity
        self.cache = OrderedDict()  # OrderedDict to keep track of access order
        
        # Performance metrics
        self.total_accesses = 0
        self.hits = 0
        self.misses = 0
    
    def access_page(self, url):
        """
        Simulate accessing a web page with the given URL.
        If the URL is in cache, it's a hit; otherwise, it's a miss.
        
        Args:
            url (str): The URL of the web page being accessed
            
        Returns:
            bool: True for hit, False for miss
        """
        self.total_accesses += 1
        
        if url in self.cache:
            # Cache hit: Move the accessed URL to the end (most recently used)
            self.cache.move_to_end(url)
            self.hits += 1
            return True
        else:
            # Cache miss: Add the URL to the cache
            self.misses += 1
            
            # If cache is full, remove the least recently used item (first item)
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                
            # Add the new URL to the cache (automatically added at the end)
            self.cache[url] = True
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
        print(f"Total page accesses: {self.total_accesses}")
        print(f"Cache hits: {self.hits}")
        print(f"Cache misses: {self.misses}")
        print(f"Hit rate: {self.get_hit_rate():.2f}%")
        print(f"Miss rate: {self.get_miss_rate():.2f}%")
        
    def get_current_cache_contents(self):
        """
        Get the current contents of the cache.
        
        Returns:
            list: List of URLs currently in the cache, from least recently used to most recently used
        """
        return list(self.cache.keys())


def simulate_different_cache_sizes(urls, cache_sizes):
    """
    Simulate cache performance for different cache sizes.
    
    Args:
        urls (list): List of URLs to simulate accesses
        cache_sizes (list): List of cache sizes to simulate
        
    Returns:
        dict: Dictionary containing performance metrics for each cache size
    """
    results = {
        'cache_sizes': cache_sizes,
        'hit_rates': [],
        'miss_rates': []
    }
    
    for size in cache_sizes:
        cache = BrowserLRUCache(size)
        
        # Process all URLs through the cache
        for url in urls:
            cache.access_page(url)
        
        # Record performance metrics
        results['hit_rates'].append(cache.get_hit_rate())
        results['miss_rates'].append(cache.get_miss_rate())
        
        # Print statistics for this cache size
        print(f"\nCache Size: {size}")
        cache.print_stats()
    
    return results


def plot_performance_comparison(results):
    """
    Plot hit rate and miss rate for different cache sizes.
    
    Args:
        results (dict): Results from simulate_different_cache_sizes
    """
    cache_sizes = results['cache_sizes']
    hit_rates = results['hit_rates']
    miss_rates = results['miss_rates']
    
    plt.figure(figsize=(10, 6))
    
    # Plot hit rates
    plt.plot(cache_sizes, hit_rates, 'o-', color='green', label='Hit Rate')
    
    # Plot miss rates
    plt.plot(cache_sizes, miss_rates, 'o-', color='red', label='Miss Rate')
    
    plt.title('Cache Performance vs. Cache Size')
    plt.xlabel('Cache Size (number of pages)')
    plt.ylabel('Rate (%)')
    plt.grid(True)
    plt.legend()
    
    # Add value labels
    for i, (hr, mr) in enumerate(zip(hit_rates, miss_rates)):
        plt.text(cache_sizes[i], hr+2, f"{hr:.1f}%", ha='center')
        plt.text(cache_sizes[i], mr-2, f"{mr:.1f}%", ha='center')
    
    plt.tight_layout()
    plt.savefig('browser_cache_performance.png')
    plt.show()
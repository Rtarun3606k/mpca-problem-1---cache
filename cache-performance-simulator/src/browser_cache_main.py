import os
import random
from cache.browser_cache_simulator import BrowserLRUCache, simulate_different_cache_sizes, plot_performance_comparison
import matplotlib.pyplot as plt

def generate_browsing_pattern(num_pages=100, num_unique_sites=20, with_locality=True):
    """
    Generate a simulated web browsing pattern.
    
    Args:
        num_pages (int): Total number of page visits to simulate
        num_unique_sites (int): Number of unique websites to include
        with_locality (bool): Whether to simulate temporal locality in browsing
        
    Returns:
        list: A list of URLs representing the browsing pattern
    """
    # Generate a set of unique website URLs
    base_urls = [f"https://site{i}.com" for i in range(num_unique_sites)]
    
    # Generate browsing pattern
    browsing_pattern = []
    
    if with_locality:
        # With temporal locality: simulate realistic browsing patterns
        # where users tend to revisit the same sites
        
        # Popular sites that will be visited more frequently (20% of sites)
        popular_sites = random.sample(base_urls, max(1, int(num_unique_sites * 0.2)))
        
        # Moderate frequency sites (30% of sites)
        moderate_sites = random.sample([url for url in base_urls if url not in popular_sites], 
                                      max(1, int(num_unique_sites * 0.3)))
        
        # Generate the browsing pattern with locality
        for i in range(num_pages):
            if i % 10 < 5:  # 50% chance to visit a popular site
                browsing_pattern.append(random.choice(popular_sites))
            elif i % 10 < 8:  # 30% chance to visit a moderate frequency site
                browsing_pattern.append(random.choice(moderate_sites))
            else:  # 20% chance to visit a rare site
                rare_sites = [url for url in base_urls if url not in popular_sites and url not in moderate_sites]
                browsing_pattern.append(random.choice(rare_sites))
    else:
        # Without locality: random selection from all sites with equal probability
        browsing_pattern = [random.choice(base_urls) for _ in range(num_pages)]
    
    return browsing_pattern

def save_browsing_pattern(browsing_pattern, filename):
    """
    Save the browsing pattern to a file.
    
    Args:
        browsing_pattern (list): List of URLs
        filename (str): Path to save the file
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        for url in browsing_pattern:
            f.write(f"{url}\n")
    print(f"Browsing pattern saved to {filename}")

def load_browsing_pattern(filename):
    """
    Load a browsing pattern from a file.
    
    Args:
        filename (str): Path to the file
        
    Returns:
        list: List of URLs
    """
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return []
    
    with open(filename, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    print(f"Loaded {len(urls)} URLs from {filename}")
    return urls

def demonstrate_lru_mechanism():
    """
    Demonstrate the LRU mechanism with a small example for educational purposes.
    """
    print("\n=== LRU Cache Mechanism Demonstration ===")
    
    # Create a small cache with capacity 3
    cache = BrowserLRUCache(3)
    
    # Sequence of page visits to demonstrate LRU behavior
    pages = [
        "https://site1.com",  # Miss (1)
        "https://site2.com",  # Miss (1, 2)
        "https://site3.com",  # Miss (1, 2, 3)
        "https://site4.com",  # Miss, evict site1 (2, 3, 4)
        "https://site2.com",  # Hit, move site2 to MRU position (3, 4, 2)
        "https://site1.com",  # Miss, evict site3 (4, 2, 1)
        "https://site2.com",  # Hit, move site2 to MRU position (4, 1, 2)
        "https://site5.com",  # Miss, evict site4 (1, 2, 5)
    ]
    
    print("Initial empty cache: []")
    
    for i, page in enumerate(pages, 1):
        was_hit = cache.access_page(page)
        status = "HIT" if was_hit else "MISS"
        
        # Show cache state after access
        cache_contents = cache.get_current_cache_contents()
        print(f"Step {i}: Access {page} - {status}")
        print(f"Cache state: {cache_contents} (LRU → MRU)")
    
    print("\nFinal cache statistics:")
    cache.print_stats()

def main():
    """
    Main function to run the browser cache simulation.
    """
    print("Browser Cache Simulator with LRU Policy")
    print("=======================================")
    
    # Demonstrate the LRU mechanism with a small example
    demonstrate_lru_mechanism()
    
    # File to store/load browsing pattern
    trace_file = os.path.join("data", "traces", "browsing_pattern.txt")
    
    # Generate or load browsing pattern
    if os.path.exists(trace_file):
        browsing_pattern = load_browsing_pattern(trace_file)
    else:
        print("\nGenerating browsing pattern with temporal locality...")
        browsing_pattern = generate_browsing_pattern(num_pages=500, num_unique_sites=50, with_locality=True)
        save_browsing_pattern(browsing_pattern, trace_file)
    
    if not browsing_pattern:
        print("No browsing pattern available. Generating a default pattern.")
        browsing_pattern = generate_browsing_pattern(num_pages=500, num_unique_sites=50)
    
    # Analyze browsing pattern
    unique_urls = set(browsing_pattern)
    print(f"\nBrowsing Pattern Analysis:")
    print(f"Total page visits: {len(browsing_pattern)}")
    print(f"Unique websites: {len(unique_urls)}")
    
    # Frequency analysis (top 5 sites)
    url_counts = {}
    for url in browsing_pattern:
        url_counts[url] = url_counts.get(url, 0) + 1
    
    print("\nTop 5 most visited sites:")
    top_sites = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    for url, count in top_sites:
        print(f"{url}: {count} visits ({count/len(browsing_pattern)*100:.1f}%)")
    
    # Simulate with different cache sizes
    print("\n=== Simulating Different Cache Sizes ===")
    cache_sizes = [5, 10, 15, 20, 25, 30]
    results = simulate_different_cache_sizes(browsing_pattern, cache_sizes)
    
    # Plot the results
    print("\nPlotting performance comparison...")
    plot_performance_comparison(results)
    
    # Visualize frequency distribution
    plt.figure(figsize=(10, 6))
    sites, counts = zip(*sorted(url_counts.items(), key=lambda x: x[1], reverse=True))
    plt.bar(range(len(counts)), counts)
    plt.title('Website Visit Frequency Distribution')
    plt.xlabel('Website Rank (by popularity)')
    plt.ylabel('Number of Visits')
    plt.tight_layout()
    plt.savefig('website_frequency.png')
    plt.show()
    
    print("\nSimulation complete. Results saved to browser_cache_performance.png and website_frequency.png")

if __name__ == "__main__":
    main()
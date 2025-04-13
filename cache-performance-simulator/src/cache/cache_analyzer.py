class CacheAnalyzer:
    """
    A class for analyzing cache performance metrics and comparing different cache configurations.
    """

    @staticmethod
    def compare_cache_performance(cache1_stats, cache2_stats):
        """
        Compare the performance of two caches based on their statistics.
        
        Args:
            cache1_stats (dict): Statistics of the first cache.
            cache2_stats (dict): Statistics of the second cache.
        
        Returns:
            str: A summary of the comparison.
        """
        comparison = []
        
        comparison.append(f"Cache 1 - Hits: {cache1_stats['hits']}, Misses: {cache1_stats['misses']}, Hit Rate: {cache1_stats['hit_rate']:.2f}%, Miss Rate: {cache1_stats['miss_rate']:.2f}%")
        comparison.append(f"Cache 2 - Hits: {cache2_stats['hits']}, Misses: {cache2_stats['misses']}, Hit Rate: {cache2_stats['hit_rate']:.2f}%, Miss Rate: {cache2_stats['miss_rate']:.2f}%")
        
        if cache1_stats['hit_rate'] > cache2_stats['hit_rate']:
            comparison.append("Cache 1 has a better hit rate.")
        elif cache1_stats['hit_rate'] < cache2_stats['hit_rate']:
            comparison.append("Cache 2 has a better hit rate.")
        else:
            comparison.append("Both caches have the same hit rate.")
        
        return "\n".join(comparison)

    @staticmethod
    def analyze_cache_statistics(cache):
        """
        Analyze and return cache statistics.
        
        Args:
            cache (CacheSimulator): An instance of the CacheSimulator class.
        
        Returns:
            dict: A dictionary containing cache statistics.
        """
        return {
            'hits': cache.hits,
            'misses': cache.misses,
            'hit_rate': cache.get_hit_rate(),
            'miss_rate': cache.get_miss_rate()
        }
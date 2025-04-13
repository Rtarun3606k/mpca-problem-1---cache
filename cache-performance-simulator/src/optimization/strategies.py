class OptimizationStrategy:
    """
    Base class for optimization strategies.
    """
    def apply(self, cache_simulator):
        """
        Apply the optimization strategy to the given cache simulator.
        
        Args:
            cache_simulator (CacheSimulator): The cache simulator to optimize.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")


class BlockSizeOptimizationStrategy:
    """
    Optimization strategy that increases the block size
    """
    def __init__(self, target_block_size=None, multiplier=2):
        """
        Initialize the strategy
        
        Args:
            target_block_size: Specific block size to use (if None, multiply existing by multiplier)
            multiplier: Factor to multiply the current block size by (default: 2)
        """
        self.target_block_size = target_block_size
        self.multiplier = multiplier
    
    def optimize(self, cache):
        """
        Apply the optimization strategy
        
        Args:
            cache: The cache simulator to optimize
            
        Returns:
            dict: Modified cache parameters
        """
        if self.target_block_size:
            new_block_size = self.target_block_size
        else:
            new_block_size = cache.block_size * self.multiplier
        
        return {'block_size': new_block_size}


class CacheSizeOptimizationStrategy:
    """
    Optimization strategy that increases the cache size
    """
    def __init__(self, target_cache_size=None, multiplier=2):
        """
        Initialize the strategy
        
        Args:
            target_cache_size: Specific cache size to use (if None, multiply existing by multiplier)
            multiplier: Factor to multiply the current cache size by (default: 2)
        """
        self.target_cache_size = target_cache_size
        self.multiplier = multiplier
    
    def optimize(self, cache):
        """
        Apply the optimization strategy
        
        Args:
            cache: The cache simulator to optimize
            
        Returns:
            dict: Modified cache parameters
        """
        if self.target_cache_size:
            new_cache_size = self.target_cache_size
        else:
            new_cache_size = cache.cache_size * self.multiplier
        
        return {'cache_size': new_cache_size}


class AssociativityOptimizationStrategy:
    """
    Optimization strategy that increases cache associativity
    """
    def __init__(self, target_associativity=2):
        """
        Initialize the strategy
        
        Args:
            target_associativity: The target associativity level
        """
        self.target_associativity = target_associativity
    
    def optimize(self, cache):
        """
        Apply the optimization strategy
        
        Args:
            cache: The cache simulator to optimize
            
        Returns:
            dict: Modified cache parameters
        """
        # Get current associativity (default to 1 if not present)
        current_associativity = getattr(cache, 'associativity', 1)
        
        # Only increase if target is higher
        if self.target_associativity > current_associativity:
            return {'associativity': self.target_associativity}
        
        return {}


# Factory function to create optimization strategies
def create_optimization_strategy(strategy_name, **kwargs):
    """
    Create an optimization strategy by name
    
    Args:
        strategy_name: Name of the strategy to create
        **kwargs: Additional parameters for the strategy
        
    Returns:
        An optimization strategy object
    """
    strategies = {
        'block_size': BlockSizeOptimizationStrategy,
        'cache_size': CacheSizeOptimizationStrategy,
        'associativity': AssociativityOptimizationStrategy
    }
    
    if strategy_name in strategies:
        return strategies[strategy_name](**kwargs)
    else:
        raise ValueError(f"Unknown optimization strategy: {strategy_name}")
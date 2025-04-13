class Optimizer:
    """
    Class to optimize cache performance using different strategies
    """
    def __init__(self, cache, strategies=None):
        """
        Initialize the optimizer
        
        Args:
            cache: The cache simulator to optimize
            strategies: List of optimization strategies to apply
        """
        self.cache = cache
        self.strategies = strategies or []
        self.optimized_cache = None
    
    def add_strategy(self, strategy):
        """
        Add an optimization strategy
        
        Args:
            strategy: The strategy to add
        """
        self.strategies.append(strategy)
    
    def apply_optimization_strategy(self):
        """
        Apply the optimization strategies to create an optimized cache
        
        Returns:
            The optimized cache simulator
        """
        # Start with a copy of the original cache configuration
        # In a real implementation, we would clone the cache
        # For now, we'll just create a new one with modified parameters
        from cache.cache_simulator import CacheSimulator
        
        # Default optimization if no strategies are provided
        # Increase block size as a simple optimization
        block_size = self.cache.block_size * 2
        cache_size = self.cache.cache_size
        associativity = getattr(self.cache, 'associativity', 1)  # Default to 1 if not present
        
        # Apply each strategy to modify cache parameters
        for strategy in self.strategies:
            if hasattr(strategy, 'optimize'):
                params = strategy.optimize(self.cache)
                if 'block_size' in params:
                    block_size = params['block_size']
                if 'cache_size' in params:
                    cache_size = params['cache_size']
                if 'associativity' in params:
                    associativity = params['associativity']
        
        # Create optimized cache
        if hasattr(self.cache, 'associativity'):
            # If it's a set-associative cache
            self.optimized_cache = CacheSimulator(
                cache_size=cache_size,
                block_size=block_size,
                associativity=associativity
            )
        else:
            # Direct-mapped cache
            self.optimized_cache = CacheSimulator(
                cache_size=cache_size,
                block_size=block_size
            )
        
        return self.optimized_cache
def analyze_access_patterns(memory_addresses):
    """
    Analyze the access patterns from a list of memory addresses.
    
    Args:
        memory_addresses (list): List of memory addresses accessed.
        
    Returns:
        dict: A dictionary containing access pattern statistics.
    """
    access_count = {}
    
    for address in memory_addresses:
        if address in access_count:
            access_count[address] += 1
        else:
            access_count[address] = 1
            
    return access_count


def generate_access_pattern_report(access_count):
    """
    Generate a report of access patterns.
    
    Args:
        access_count (dict): Dictionary containing access counts for each address.
        
    Returns:
        str: A formatted string report of access patterns.
    """
    report_lines = ["Access Pattern Report:"]
    report_lines.append(f"{'Address':<15} {'Count':<10}")
    report_lines.append("-" * 25)
    
    for address, count in access_count.items():
        report_lines.append(f"{address:<15} {count:<10}")
        
    return "\n".join(report_lines)
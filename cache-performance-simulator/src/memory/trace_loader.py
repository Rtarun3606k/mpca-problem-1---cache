def load_memory_trace(file_path):
    """
    Load memory addresses from a trace file into a list.
    
    Args:
        file_path (str): Path to the memory trace file.
        
    Returns:
        list: A list of memory addresses.
    """
    addresses = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and convert to integer
                address = line.strip()
                if address:
                    addresses.append(int(address, 16))  # Assuming addresses are in hexadecimal
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError:
        print("Error: Invalid address format in the trace file.")
    
    return addresses
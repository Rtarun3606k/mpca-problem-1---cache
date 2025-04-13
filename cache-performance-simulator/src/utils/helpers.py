def load_memory_trace(file_path):
    with open(file_path, 'r') as file:
        addresses = [int(line.strip()) for line in file if line.strip().isdigit()]
    return addresses

def save_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"{result}\n")

def print_memory_trace(addresses):
    print("Memory Access Trace:")
    for address in addresses:
        print(f"Address: {address}")
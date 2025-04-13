def generate_chart(data, title="Cache Performance", xlabel="Accesses", ylabel="Count"):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(data['accesses'], data['hits'], label='Hits', color='green', marker='o')
    plt.plot(data['accesses'], data['misses'], label='Misses', color='red', marker='o')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
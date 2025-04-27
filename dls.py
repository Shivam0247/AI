def dls(graph, current, destination, limit):
    if current == destination:
        return True
    if limit <= 0:
        return False

    for neighbor in graph.get(current, []):
        if dls(graph, neighbor, destination, limit - 1):
            return True

    return False

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# User input
source = input("Enter source node: ")
destination = input("Enter destination node: ")
limit = int(input("Enter depth limit: "))

# Run DLS
found = dls(graph, source, destination, limit)

if found:
    print(f"\nPath found from {source} to {destination} within depth {limit}.")
else:
    print(f"\nNo path found from {source} to {destination} within depth {limit}.")

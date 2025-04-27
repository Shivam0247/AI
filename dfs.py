def dfs(graph, source, destination, visited=None):
    if visited is None:
        visited = set()
    visited.add(source)
    print(source, end=" ")

    if source == destination:
        print("\nDestination found!")
        return True

    for neighbor in graph.get(source, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, destination, visited):
                return True
    return False

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

source = input("Enter source node: ")
destination = input("Enter destination node: ")

print("\nDFS Traversal:")
found = dfs(graph, source, destination)
if not found:
    print("\nDestination not found!")

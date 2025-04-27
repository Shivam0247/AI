def dfs_limited(graph, node, destination, depth, visited):
    if depth == 0 and node == destination:
        print(f"Found destination: {node}")
        return True
    if depth > 0:
        visited.add(node)
        print(f"Visiting: {node}, Remaining Depth: {depth}")
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs_limited(graph, neighbor, destination, depth - 1, visited):
                    return True
        visited.remove(node)
    return False

def iddfs(graph, start, destination):
    depth = 0
    while True:
        print(f"\nStarting DFS with depth limit: {depth}")
        visited = set()
        if dfs_limited(graph, start, destination, depth, visited):
            print(f"\nDestination {destination} found at depth {depth}!")
            break
        depth += 1

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = input("Enter start node: ").strip()
destination = input("Enter destination node: ").strip()

print("\nIterative Deepening DFS Traversal:")
iddfs(graph, start, destination)

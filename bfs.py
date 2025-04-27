from collections import deque

def bfs(graph, source, destination):
    visited = set()
    queue = deque([source])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        if node == destination:
            print("\nDestination found!")
            return True
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
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

print("\nBFS Traversal:")
found = bfs(graph, source, destination)
if not found:
    print("\nDestination not found!")

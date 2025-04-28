# Function to input graph as adjacency matrix
def input_graph():
    n = int(input("Enter number of nodes: "))
    graph = [[int(input(f"Edge {i} -> {j} (1/0): ")) for j in range(n)] for i in range(n)]
    src = int(input("Enter source node: "))
    goal = int(input("Enter goal node: "))
    return graph, src, goal

# Breadth-First Search
def bfs(graph, src, goal):
    queue = [(src, [src])]
    visited = set()

    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        visited.add(node)
        for neighbor, connected in enumerate(graph[node]):
            if connected and neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# Depth-First Search
def dfs(graph, src, goal):
    stack = [(src, [src])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        visited.add(node)
        for neighbor, connected in enumerate(graph[node]):
            if connected and neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# Main function
if __name__ == "__main__":
    graph, src, goal = input_graph()

    bfs_path = bfs(graph, src, goal)
    dfs_path = dfs(graph, src, goal)

    if bfs_path:
        print(f"\nBFS Path from {src} to {goal}: {bfs_path}")
    else:
        print("\nNo path found using BFS.")

    if dfs_path:
        print(f"DFS Path from {src} to {goal}: {dfs_path}")
    else:
        print("No path found using DFS.")

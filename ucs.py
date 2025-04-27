import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, node)
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)  # Get the node with least cost

        if node == goal:
            print(f"Destination '{goal}' found with total cost: {cost}")
            return True

        if node not in visited:
            print(f"Visiting: {node} with cost {cost}")
            visited.add(node)

            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))

    print("Destination not found!")
    return False

# Example weighted graph
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

print("\nUniform Cost Search Traversal:")
uniform_cost_search(graph, start, goal)

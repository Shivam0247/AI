import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = []
    
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        print(f"Visiting: {current}")

        if current == goal:
            print("\nGoal found!")
            return True

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    print("\nGoal not reachable.")
    return False

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Example heuristic values (smaller = better, closer to goal)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 6,
    'E': 2,
    'F': 0
}

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

print("\nBest-First Search Traversal:")
found = best_first_search(graph, start, goal, heuristic)  # Pass the heuristic here

if not found:
    print("Destination not found!")

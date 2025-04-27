import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    closed_list = set()
    g = {start: 0}  # g(n) for each node
    f = {start: heuristic[start]}  # f(n) for each node
    came_from = {}  # to store the path
    
    # Add the start node to the open list
    heapq.heappush(open_list, (f[start], start))
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            print("\nPath found:", " -> ".join(path))
            return path
        
        closed_list.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor in closed_list:
                continue
            
            tentative_g = g[current] + 1  # Assuming uniform cost (1 step)
            
            if neighbor not in g or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                f[neighbor] = g[neighbor] + heuristic.get(neighbor, 0)
                came_from[neighbor] = current
                heapq.heappush(open_list, (f[neighbor], neighbor))
    
    print("\nGoal not reachable.")
    return None

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example heuristic values (smaller = better, closer to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 0
}

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

print("\nA* Search Traversal:")
path = a_star_search(graph, start, goal, heuristic)

if path:
    print("Goal found!")
else:
    print("Destination not found!")

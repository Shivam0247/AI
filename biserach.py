from collections import deque

def bfs_step(queue, visited, other_visited, graph):
    if queue:
        current = queue.popleft()
        print(f"Visiting: {current}")
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
                if neighbor in other_visited:
                    return neighbor
    return None

def bidirectional_search(graph, start, goal):
    if start == goal:
        print("Start is the Goal!")
        return [start]

    # Two queues for forward and backward search
    queue_start = deque([start])
    queue_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:
        # Forward Search Step
        meeting_node = bfs_step(queue_start, visited_start, visited_goal, graph)
        if meeting_node:
            return construct_path(visited_start, visited_goal, meeting_node)

        # Backward Search Step
        meeting_node = bfs_step(queue_goal, visited_goal, visited_start, graph)
        if meeting_node:
            return construct_path(visited_start, visited_goal, meeting_node)

    return None

def construct_path(visited_start, visited_goal, meeting_node):
    # Build path from start to meeting node
    path = []
    node = meeting_node
    while node:
        path.append(node)
        node = visited_start[node]
    path = path[::-1]  # reverse the first half

    # Build path from meeting node to goal
    node = visited_goal[meeting_node]
    while node:
        path.append(node)
        node = visited_goal[node]
    
    return path

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

print("\nBidirectional Search Traversal:")
path = bidirectional_search(graph, start, goal)

if path:
    print(f"\nPath found: {' -> '.join(path)}")
else:
    print("\nNo path found between the nodes.")

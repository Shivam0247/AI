def is_goal(state, goal):
    return state[0] == goal or state[1] == goal

def print_solution(path):
    print("\nSteps to reach the goal:")
    for state in path:
        print(f"Jug1: {state[0]} liters, Jug2: {state[1]} liters")

def water_jug_bfs(capacityA, capacityB, goal):
    visited = set()
    queue = []  # Simple list instead of deque
    
    # Start from (0, 0)
    queue.append([(0, 0)])
    visited.add((0, 0))
    
    while queue:
        path = queue.pop(0)  # pop first element (FIFO behavior)
        current = path[-1]
        
        if is_goal(current, goal):
            print("\nGoal achieved!")
            print_solution(path)
            return
        
        x, y = current
        
        # List of all possible next moves
        moves = [
            (capacityA, y),        # Fill jug1
            (x, capacityB),        # Fill jug2
            (0, y),                # Empty jug1
            (x, 0),                # Empty jug2
            (x - min(x, capacityB - y), y + min(x, capacityB - y)),  # Pour jug1 -> jug2
            (x + min(y, capacityA - x), y - min(y, capacityA - x))   # Pour jug2 -> jug1
        ]
        
        for move in moves:
            if move not in visited:
                visited.add(move)
                new_path = path + [move]
                queue.append(new_path)
    
    print("\nNo solution found!")

# ------------------
# Test the function
capacityA = 4  # Capacity of Jug 1
capacityB = 3  # Capacity of Jug 2
goal = 2       # Goal amount

water_jug_bfs(capacityA, capacityB, goal)

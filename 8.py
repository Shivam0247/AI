from collections import deque

# Function to print the 3x3 puzzle
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Function to generate the next valid states from the current state
def get_neighbors(state):
    neighbors = []
    # Find the position of the blank space (0)
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                blank_pos = (r, c)
                break
    
    row, col = blank_pos
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:  # Check if within bounds
            new_state = [row.copy() for row in state]  # Create a deep copy of the state
            # Swap the blank space with the adjacent tile
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append(new_state)
    
    return neighbors

# Function to perform BFS and find the solution
def bfs(initial_state, goal_state):
    # Queue to store the current state and path taken to reach it
    queue = deque([(initial_state, [])])
    
    # Set to store visited states (as tuples of tuples for immutability)
    visited = set()
    visited.add(tuple(tuple(row) for row in initial_state))  # Convert to tuple of tuples for immutability
    
    while queue:
        current_state, path = queue.popleft()
        
        # If we reach the goal state, return the path
        if current_state == goal_state:
            return path
        
        # Generate neighbors (valid states)
        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)  # Convert to tuple of tuples for immutability
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                # Add the neighbor state and the move made to reach it
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No solution found

# Example usage
initial_state = [[1, 2, 3], 
                 [4, 0, 5], 
                 [6, 7, 8]]  # Initial configuration

goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]  # Goal configuration

# Perform BFS to find the solution path
solution_path = bfs(initial_state, goal_state)

if solution_path:
    print("Solution found in", len(solution_path), "steps.")
    for step in solution_path:
        print_puzzle(step)
else:
    print("No solution found.")

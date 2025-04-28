# Define the goal state for the 8-puzzle problem
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Define the possible moves: up, down, left, right
# These are the indexes for a 3x3 grid, where 0 represents the empty space

def get_possible_moves(state):
    """
    Given the current state of the puzzle, return a list of states
    that can be reached by making valid moves (up, down, left, right).
    """
    moves = []
    index = state.index(0)  # Find the index of the empty space (0)

    # Define possible move directions (up, down, left, right)
    directions = {
        'up': index - 3 if index >= 3 else -1,
        'down': index + 3 if index <= 5 else -1,
        'left': index - 1 if index % 3 != 0 else -1,
        'right': index + 1 if index % 3 != 2 else -1,
    }

    # Try to make a move in each direction and check if it's valid
    for direction, new_index in directions.items():
        if new_index != -1:  # Valid move
            new_state = state[:]
            # Swap the empty space (0) with the target position
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            moves.append(new_state)

    return moves

def dfs(state, path, visited):
    """
    Perform Depth-First Search (DFS) to find the solution to the 8-puzzle.
    The function returns the solution path if found.
    """
    # Check if the current state is the goal state
    if state == GOAL_STATE:
        return path + [state]
    
    # Mark the current state as visited
    visited.add(tuple(state))
    
    # Explore possible moves
    for next_state in get_possible_moves(state):
        if tuple(next_state) not in visited:
            result = dfs(next_state, path + [state], visited)
            if result:
                return result
    
    # No solution found on this path
    return None

def solve_8_puzzle(initial_state):
    """
    Solves the 8-puzzle using Depth-First Search (DFS).
    """
    visited = set()  # Set to store visited states
    solution_path = dfs(initial_state, [], visited)
    
    if solution_path:
        for step in solution_path:
            print(step)
    else:
        print("No solution found.")

# Example initial state of the puzzle
initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]

# Solve the puzzle
solve_8_puzzle(initial_state)

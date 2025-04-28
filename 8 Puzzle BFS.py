class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.rows = 3
        self.cols = 3

    def get_blank_position(self, state):
        """Find the position of the blank tile (0) in the current state."""
        for i in range(self.rows):
            for j in range(self.cols):
                if state[i][j] == 0:
                    return i, j
        return None

    def generate_new_states(self, state):
        """Generate all possible states by moving the blank tile."""
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        blank_x, blank_y = self.get_blank_position(state)
        new_states = []
        
        for move in moves:
            new_x, new_y = blank_x + move[0], blank_y + move[1]
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                new_state = [row[:] for row in state]  # Copy current state
                # Swap blank tile with the adjacent tile
                new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
                new_states.append(new_state)
        
        return new_states

    def bfs(self):
        """Breadth-First Search to find the solution."""
        queue = [(self.initial_state, [])]  # (Current state, Path to reach state)
        visited = set()
        
        while queue:
            state, path = queue.pop(0)  # Dequeue the first element (FIFO)
            
            if state == self.goal_state:
                return path + [state]  # Return the path including the goal state
            
            # Mark the state as visited
            visited.add(tuple(map(tuple, state)))
            
            # Generate and enqueue all possible new states
            for new_state in self.generate_new_states(state):
                if tuple(map(tuple, new_state)) not in visited:
                    queue.append((new_state, path + [state]))
        
        return None  # Return None if no solution is found

    def print_solution(self, solution):
        """Display the solution path."""
        if not solution:
            print("No solution found")
        else:
            for step_num, step in enumerate(solution):
                print(f"Step {step_num}:")
                for row in step:
                    print(row)
                print("---")


# Example Usage
initial_state = [[1, 2, 3], 
                 [4, 0, 5], 
                 [6, 7, 8]]

goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]

# Create Puzzle instance
puzzle = Puzzle(initial_state, goal_state)

# Find solution using BFS
solution = puzzle.bfs()

# Print the solution steps
puzzle.print_solution(solution)

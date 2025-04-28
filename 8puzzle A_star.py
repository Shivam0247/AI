import numpy as np

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.depth) < (other.cost + other.depth)

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = np.where(goal == state[i][j])
                distance += abs(i - x[0]) + abs(j - y[0])
    return distance

def get_possible_moves(state):
    moves = []
    x, y = np.where(state == 0)
    x, y = x[0], y[0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = state.copy()
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append((new_state, (new_x, new_y)))
    
    return moves

def a_star_search(start, goal):
    priority_queue = [PuzzleNode(start, cost=manhattan_distance(start, goal))]
    visited = set()
    
    while priority_queue:
        priority_queue.sort()  # Sort based on cost + depth
        current_node = priority_queue.pop(0)
        
        if np.array_equal(current_node.state, goal):
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        
        visited.add(tuple(map(tuple, current_node.state)))
        
        for new_state, _ in get_possible_moves(current_node.state):
            if tuple(map(tuple, new_state)) not in visited:
                priority_queue.append(PuzzleNode(new_state, current_node, depth=current_node.depth + 1, cost=manhattan_distance(new_state, goal)))
    
    return None

def print_puzzle_solution(solution):
    if not solution:
        print("No solution found")
    else:
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print(state, "\n")

if __name__ == "__main__":
    start_state = np.array([[1, 4, 3], [2, 0, 7], [6, 5, 8]])
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    
    solution = a_star_search(start_state, goal_state)
    print_puzzle_solution(solution)

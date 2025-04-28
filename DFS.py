# Input: Adjacency matrix and source/goal nodes
def graph_input():
    d_mtx = []
    n = int(input("Enter the number of nodes in the graph: "))
    print("Enter the existence of edges between nodes (1 for edge, 0 for no edge):")

    # Building the adjacency matrix
    for i in range(n):
        d_mtx.append([])
        for j in range(n):
            d_mtx[-1].append(int(input(f"Edge between node {i} and node {j}: ")))

    s = int(input("Enter the index number of the source node: "))
    g = int(input("Enter the index number of the goal node: "))
    return d_mtx, n, s, g

# DFS Algorithm
def dfs_algorithm(d_mtx, n, s, g):
    print("\nRunning DFS...")
    stack = [s]  # Stack to store nodes to visit
    visited = [s]  # List to keep track of visited nodes
    paths = [[s]]  # List to store paths

    if s == g:
        print(f"Goal node {g} found in DFS from {s}")
        print(f"Path traversed: {paths[0]}")
        return

    found = False
    while stack:
        node = stack.pop()  # Pop the top element
        path = paths.pop()  # Get the corresponding path

        for i in range(n):
            if d_mtx[node][i] == 1:  # Check if there's an edge
                if i == g:  # Goal found
                    print(f"Goal node {i} found in DFS from {s}")
                    print(f"Traversal path found using DFS: {path + [i]}")
                    print(f"Nodes checked in DFS: {visited + [i]}")
                    found = True
                    break
                if i not in visited:  # If not visited
                    stack.append(i)
                    visited.append(i)
                    paths.append(path + [i])

        if found:
            break

    if not found:
        print(f"Goal node {g} not found in DFS from {s}")

# Main function
if __name__ == "__main__":
    d_mtx, n, s, g = graph_input()

    # Validate source and goal nodes
    if 0 <= s < n and 0 <= g < n:
        dfs_algorithm(d_mtx, n, s, g)
    else:
        print(f"Invalid node indices. The values must be in the range [0, {n-1}]")

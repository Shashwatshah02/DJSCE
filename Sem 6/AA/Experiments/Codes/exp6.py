def ford_fulkerson(G, source, sink):
    max_flw = 0  # Initialize maximum flow
    allpath, path_flws = [], []  # Lists to store all augmenting paths and their corresponding flows
    while True:
        paths = bfs(G, source, sink)  # Find all augmenting paths using BFS
        if not paths:  # If no more augmenting paths exist, exit the loop
            break
        for path in paths:  # Iterate over each augmenting path
            # Compute flow along the path as the minimum capacity of edges in the path
            path_flw = min(G[path[i]][path[i+1]] for i in range(len(path)-1))
            allpath.append(path)  # Store the augmenting path
            path_flws.append(path_flw)  # Store the flow along the augmenting path
            max_flw += path_flw  # Update the maximum flow
            G = modify_G(G, path, path_flw)  # Modify the graph by updating edge capacities
    return max_flw, allpath, path_flws  # Return the maximum flow and augmenting paths with flows

def bfs(G, source, sink):
    paths = []  # List to store all found paths
    queue = [(source, [source])]  # Initialize BFS queue with source node and its path
    front = 0  # Front index of the BFS queue
    while front < len(queue):  # While there are nodes in the BFS queue
        u, path = queue[front]  # Dequeue a node and its path
        front += 1  # Move to the next node in the queue
        for v, capacity in enumerate(G[u]):  # Iterate over neighbors of the dequeued node
            if capacity > 0 and v not in path:  # If there is residual capacity and neighbor is not visited
                if v == sink:  # If neighbor is the sink, a path is found
                    paths.append(path + [v])  # Add the complete path to paths list
                else:
                    queue.append((v, path + [v]))  # Enqueue the neighbor with its updated path
    return paths  # Return all found paths

def modify_G(G, path, flw):
    # Modify the graph G by updating edge capacities along the given path
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]  # Get current edge endpoints
        G[u][v] -= flw  # Decrease capacity of forward edge
        G[v][u] += flw  # Increase capacity of backward edge (residual graph)
    return G  # Return the modified graph

# Example graph representation (adjacency matrix)
G = [[0, 9, 8, 0, 0, 0],
     [0, 0, 0, 4, 4, 0],
     [0, 2, 0, 0, 5, 3],
     [0, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 0, 6],
     [0, 0, 0, 0, 0, 0]]

source = 0  # Source node
sink = 5  # Sink node
max_flw, allpath, path_flws = ford_fulkerson(G, source, sink)  # Apply Ford-Fulkerson algorithm
print(f"Maximum flow: {max_flw}")  # Print the maximum flow
print("<-----All augmenting paths and their corresponding flows----->")
for i, path in enumerate(allpath):  # Print all augmenting paths and their flows
    print(f"Path --> {path}, flow along path: {path_flws[i]}")

def fordFulkerson(G, source, sink):
    max_flow = 0
    augumented_paths, path_flows = [], [] 
    while True:
        paths = bfs(G, source, sink)
        if not paths:
            break
        for path in paths:
            path_flow = min(G[path[i]][path[i+1]] for i in range(len(path)-1))
            augumented_paths.append(path)
            path_flows.append(path_flow)
            max_flow += path_flow
            G = modify(G, path, path_flow)
        return max_flow, augumented_paths, path_flows
def bfs(G, source, sink):
    paths = []
    queue = [(source, [source])]
    pointer = 0
    while pointer < len(queue):
        u, visited = queue[pointer]
        pointer += 1
        for v, capacity in enumerate(G[u]):
            if capacity>0 and v not in visited:
                if v == sink:
                    paths.append(visited + [v])
                else:
                    queue.append((v, visited+[v]))
    return paths

def modify(G, path, flow):
    for i in range(len(path)-1):
        u,v =path[i], path[i+1]
        G[u][v] -= flow
        G[v][u] += flow
    return G


G = [[0, 9, 8, 0, 0, 0],
     [0, 0, 0, 4, 4, 0],
     [0, 2, 0, 0, 5, 3],
     [0, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 0, 6],
     [0, 0, 0, 0, 0, 0]]

source = 0  # Source node
sink = 5  # Sink node

max_flow, augumented_paths, path_flows = fordFulkerson(G, 0, 5)
print("Max flow: ", max_flow)
for i, path in enumerate(augumented_paths):
    print(f"Path --> ", path, "Minimum possible flow is", path_flows[i])
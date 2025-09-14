def dfs(adj, col, node, color):
    color[node] = col
    for nei in adj[node]:
        if color[nei]==-1:
            if not dfs(adj,1-col,nei,color):
                return False
        elif color[nei]==col:
            return False
    return True


def isBipartite(graph):
    """
    Checks if a graph is bipartite using Depth-First Search (DFS).

    Args:
        graph: An adjacency list representation of the graph.
               Example: {0: [1, 3], 1: [0, 2], ...}

    Returns:
        True if the graph is bipartite, False otherwise.
    """
    num_nodes = len(graph)
    color = [-1] * num_nodes  # -1: uncolored, 0: color 1, 1: color 2

    # This loop handles disconnected components in the graph
    for i in range(num_nodes):
        if color[i] == -1:
            # Start DFS from this uncolored node
            if not dfs(i, graph, 0, color):
                return False

    return True
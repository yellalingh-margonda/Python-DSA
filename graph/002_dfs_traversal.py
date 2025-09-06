adj_list={0: [1, 2],
1: [0, 3, 4],
2: [0, 4],
3: [1, 5],
4: [1, 2, 5],
5: [3, 4],
 }
nodes=6
def dfs(adj, current_node,nodes,visited=None, ans=None):
    if visited is None:
        visited=[False]*nodes
    if ans is None:
        ans = []
    ans.append(current_node)
    visited[current_node]=True
    for nei in adj[current_node]:
        if not visited[nei]:
            dfs(adj,nei,nodes,visited,ans)
    return ans

adj_list={0: [1, 2],
1: [0, 3, 4],
2: [0, 4],
3: [1, 5],
4: [1, 2, 5],
5: [3, 4],
 }
nodes=6

def bfs(adj,nodes):
    visited=[False]*nodes
    ans=[]
    visited[3]=True
    queue=[3]
    while queue:
        node=queue.pop(0)
        ans.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)
    return ans


print(bfs(adj_list,nodes))


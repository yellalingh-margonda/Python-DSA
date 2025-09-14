from collections import deque
def canfinish(nodes, prerequest):
    preMap = {i: [] for i in range(nodes)}
    for cur, pre in prerequest:
        preMap[cur].append(pre)
    indegr={crs:0 for crs in range(nodes)}
    for i in range(nodes):
        for v in nodes[i]:
            indegr[v]+=1
    stack=deque([ele for ele in range(nodes) if indegr[ele]==0])
    topo=[]
    while stack:
        node=stack.popleft()
        topo.append(node)
        for nei in preMap[node]:
            indegr[nei]-=1
            if indegr[nei]==0:
                stack.append(nei)
    return len(topo)==nodes


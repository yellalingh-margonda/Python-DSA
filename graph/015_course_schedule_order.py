from collections import deque


def canfinish(nodes, prerequest):
    # build adjacency list: pre -> [cur]
    preMap = {i: [] for i in range(nodes)}
    indegr = {i: 0 for i in range(nodes)}

    for cur, pre in prerequest:
        preMap[pre].append(cur)
        indegr[cur] += 1

    # queue of courses with no prerequisites
    stack = deque([i for i in range(nodes) if indegr[i] == 0])
    topo = []

    while stack:
        node = stack.popleft()
        topo.append(node)
        for nei in preMap[node]:
            indegr[nei] -= 1
            if indegr[nei] == 0:
                stack.append(nei)

    return topo

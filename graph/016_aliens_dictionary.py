from collections import deque, defaultdict

def alien_dictionary(words):
    # Step 1: Build graph (adj list) and indegree map
    unique_chars = set("".join(words))
    graph = defaultdict(list)
    indegree = {ch: 0 for ch in unique_chars}

    # Step 2: Build edges from word comparisons
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]

        # invalid case: prefix issue
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
                break
    # Step 3: BFS Topological Sort
    queue = deque([ch for ch in indegree if indegree[ch] == 0])
    topo = []

    while queue:
        ch = queue.popleft()
        topo.append(ch)
        for nei in graph[ch]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    # Step 4: Check if topo contains all chars
    if len(topo) != len(unique_chars):
        return ""

    return "".join(topo)
print(alien_dictionary(["wrt", "wrf", "er", "ett", "rftt"]))
# Possible output: "wertf"

print(alien_dictionary(["z", "x"]))
# "zx" or "xz" depending on graph

print(alien_dictionary(["abc", "ab"]))
# ""

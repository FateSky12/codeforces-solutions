from heapq import heappop, heappush

def dijkstra(n, edges):
    g = [[] for _ in range(n)] # 通常使用邻接表建图即可，因为对于稀疏图邻接矩阵会浪费大量空间，而稠密图两者差距不大
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w)) # 无向图相当于有两个方向的边，如果单向图则不需要这一行

    dist = [float('inf')] * n
    dist[0] = 0
    h = [(0, 0)]
    while h:
        d, u = heappop(h)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(h, (dist[v], v))

    return dist

n = 4
edges = [(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 0, 4)]
print(dijkstra(n, edges))  # [0, 1, 3, 4]

n = 1
edges = []
print(dijkstra(n, edges))  # [0]

n = 3
edges = []
print(dijkstra(n, edges))  # [0, inf, inf]
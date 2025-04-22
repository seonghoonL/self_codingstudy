import sys
input = sys.stdin.readline
import heapq
n, d = map(int, input().strip().split())
graph = [[]for _ in range(d+1)]
for _ in range(n):
    start, end, length = map(int, input().strip().split())
    if end > d:
        continue
    graph[start].append((end,length))
for i in range(d):
    graph[i].append((i+1,1))
def dijkstra(start):
    road = [float('inf')] * (d+1)
    road[start] = 0
    queue = [(0, start)]
    while queue:
        dist, now = heapq.heappop(queue)
        if dist > road[now]:
            continue
        for n_node, we in graph[now]:
            cost = dist + we
            if cost < road[n_node]:
                road[n_node] = cost
                heapq.heappush(queue, (cost, n_node))
    return road[d]
print(dijkstra(0))
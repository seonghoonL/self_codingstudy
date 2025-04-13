import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(1)
print(visited.count(True) - 1)
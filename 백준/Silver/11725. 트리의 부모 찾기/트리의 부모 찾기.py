import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(start):
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for ne in graph[node]:
            if not visited[ne]:
                parent[ne] = node
                visited[ne] = True
                stack.append(ne)
dfs(1)
for i in range(2, n + 1):
    print(parent[i])
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                stack.append(n)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def dfs(x, y):
    visited[y][x] = True
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and field[ny][nx] == 1:
                dfs(nx, ny)
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    print(count)
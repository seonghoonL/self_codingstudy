import sys
input = sys.stdin.readline
n = int(input())
grid = [list(input().strip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs():
    visited = [[False] * n for _ in range(n)]
    count = 0
    def dfs(x, y, color):
        stack = [(x, y)]
        visited[y][x] = True
        while stack:
            cx, cy = stack.pop()
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]
                if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                    if grid[ny][nx] == color:
                        visited[ny][nx] = True
                        stack.append((nx, ny))
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(j, i, grid[i][j])
                count += 1
    return count
def rgdfs():
    visited = [[False] * n for _ in range(n)]
    count = 0
    def dfs(x, y, color):
        stack = [(x, y)]
        visited[y][x] = True
        while stack:
            cx, cy = stack.pop()
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]
                if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                    if (color in "RG" and grid[ny][nx] in "RG") or (color == "B" and grid[ny][nx] == "B"):
                        visited[ny][nx] = True
                        stack.append((nx, ny))
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(j, i, grid[i][j])
                count += 1
    return count
print(dfs(), rgdfs())
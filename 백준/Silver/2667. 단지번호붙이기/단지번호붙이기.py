import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
grid = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    row = list(map(int,input().strip()))
    grid.append(row)
def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    count = 1
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    count+=1
    return count
homecount = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            homecount.append(bfs(i,j))
homecount.sort()
print(len(homecount))
for count in  homecount:
    print(count)
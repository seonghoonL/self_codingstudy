import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int,input().split())
box = [list(map(int,input().strip().split()))for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nx][ny] != 0:
                continue
            box[nx][ny] = box[x][y] +1
            queue.append((nx,ny))
    maxv = max(map(max, box)) - 1
    for row in box:
        if 0 in row:
            return -1
    if maxv == 1:
        return 0
    return maxv
print(bfs())
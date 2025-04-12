import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
maze = [list(map(int,input().strip())) for _ in range(n)] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while queue:
        x,y,f = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0 and visited[nx][ny][f] == 0:
                visited[nx][ny][f] = visited[x][y][f] + 1
                queue.append((nx, ny, f))
            elif maze[nx][ny] == 1 and f == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

    end_not_f = visited[n-1][m-1][0]
    end_f = visited[n-1][m-1][1]
    if end_not_f and end_f:
        return min(end_not_f, end_f)
    elif end_not_f:
        return end_not_f
    elif end_f:
        return end_f
    else:
        return -1
print(bfs())
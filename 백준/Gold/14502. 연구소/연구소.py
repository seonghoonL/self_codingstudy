import sys
from collections import deque
import copy
input = sys.stdin.readline
n, m = map(int,input().strip().split())
board = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs():
    queue = deque()
    tmp_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if tmp_board[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_board[nx][ny] == 0:
                tmp_board[nx][ny] = 2
                queue.append((nx,ny))
    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp_board[i].count(0)
    answer = max(answer, cnt)
def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makewall(cnt+1)
                board[i][j] = 0
for i in range(n):
    board.append(list(map(int, input().split())))
answer = 0
makewall(0)
print(answer)
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
l = int(input())
turn = dict()
for _ in range(l):
    x, c = input().split()
    turn[int(x)] = c
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direc = 0
snake = deque()
snake.append((0,0))
time = 0
x, y = 0, 0
while True:
    time += 1
    nx = x + dx[direc]
    ny = y + dy[direc]
    if not (0<= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break
    snake.appendleft((nx, ny))
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        snake.pop()
    x, y = nx, ny
    if time in turn:
        if turn[time] == 'L':
            direc = (direc - 1) % 4
        else:
            direc = (direc + 1) % 4
print(time)
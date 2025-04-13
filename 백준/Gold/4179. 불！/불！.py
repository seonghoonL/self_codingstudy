import sys
input = sys.stdin.readline
from collections import deque
r, c = map(int,input().split())
maze = [list(input().strip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    fire_q = deque()
    play_q = deque()
    fire_cnt = [[-1]*c for _ in range(r)]
    play_cnt = [[-1]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'F':
                fire_q.append((i,j))
                fire_cnt[i][j] = 0
            elif maze[i][j] =='J':
                play_q.append((i,j))
                play_cnt[i][j] = 0
    while fire_q:
        x,y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] != '#' and fire_cnt[nx][ny] == -1:
                    fire_cnt[nx][ny] = fire_cnt[x][y] + 1
                    fire_q.append((nx, ny))
    while play_q:
        x, y = play_q.popleft()
        if x == 0 or x == r-1 or y == 0 or y == c-1:
            print(play_cnt[x][y] + 1)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] != '#' and play_cnt[nx][ny] == -1:
                    if fire_cnt[nx][ny] == -1 or play_cnt[x][y] + 1 < fire_cnt[nx][ny]:
                        play_cnt[nx][ny] = play_cnt[x][y] + 1
                        play_q.append((nx, ny))
    print('IMPOSSIBLE')
bfs()
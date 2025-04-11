from collections import deque
import sys
input = sys.stdin.readline
f, s, g, u, d = map(int,input().split())
check = [-1 for _ in range(f+1)]
def bfs():
    queue = deque()
    queue.append(s)
    check[s] = 0
    while queue:
        y = queue.popleft()
        if y == g:
            return check[y]
        else:
            for x in (y + u, y - d):
                if (0 < x <= f) and check[x] == -1:
                    check[x] = check[y] + 1
                    queue.append(x)
    return 'use the stairs'
print(bfs())
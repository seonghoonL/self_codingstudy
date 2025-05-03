import sys
import bisect
input = sys.stdin.readline
N, H = map(int,input().split())
down = []
up = []
for i in range(N):
    a = int(input())
    if i % 2 == 0:
        down.append(a)
    else:
        up.append(a)
down.sort()
up.sort()
count = 0
for i in range(1, H + 1):
    down_c = len(down) - bisect.bisect_left(down, i)
    up_c = len(up) - bisect.bisect_left(up, H - i + 1)
    total = down_c + up_c
    if total == N:
        count+=1
    elif total < N:
        N = total
        count = 1
print(N, count)
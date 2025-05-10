import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    tong = [0] * N
    left = 0
    right = N - 1
    for i in range(N):
        if i % 2 == 0:
            tong[left] = logs[i]
            left += 1
        else:
            tong[right] = logs[i]
            right -= 1
    md = 0
    for i in range(N):
        di = abs(tong[i] - tong[(i + 1) % N])
        md = max(md, di)
    print(md)
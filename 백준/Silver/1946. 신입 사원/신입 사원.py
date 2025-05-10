import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    jiwon = [tuple(map(int, input().split())) for _ in range(N)]
    jiwon.sort()
    count = 1
    bi = jiwon[0][1]
    for i in range(1, N):
        if jiwon[i][1] < bi:
            count += 1
            bi = jiwon[i][1]
    print(count)
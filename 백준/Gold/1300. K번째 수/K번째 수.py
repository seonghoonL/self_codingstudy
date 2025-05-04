import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
left, right = 1, K
result = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(1,N+1):
        count += min(N, mid // i)
    if count >= K:
        result = mid
        right = mid -1
    else:
        left = mid + 1
print(result)
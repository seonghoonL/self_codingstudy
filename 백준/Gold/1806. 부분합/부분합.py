import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
min_length = n + 1
cnt = 0
left = 0
for right in range(n):
    cnt += arr[right]
    while cnt >= s:
        min_length = min(min_length, right - left + 1)
        cnt -= arr[left]
        left += 1
if min_length != n + 1:
    print(min_length)
else:
    print(0)
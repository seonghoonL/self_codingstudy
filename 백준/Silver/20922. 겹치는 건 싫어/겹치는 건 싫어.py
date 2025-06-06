import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int,input().split())
arr = list(map(int, input().split()))
count = defaultdict(int)
left = 0
max_len = 0
for right in range(n):
    count[arr[right]] += 1
    while count[arr[right]] > k:
        count[arr[left]] -= 1
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)
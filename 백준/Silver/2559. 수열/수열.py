import sys
input = sys.stdin.readline
n, k = map(int,input().split())
temp = list(map(int,input().split()))
window = sum(temp[:k])
ms = window
for i in range(k, n):
    window = window - temp[i-k] + temp[i]
    if window > ms:
        ms = window
print(ms)
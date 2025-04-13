import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if a[i] in d:
        print(d[a[i]] + 1, i + 1)
        break
    d[a[i]] = i
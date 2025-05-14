import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
sour = []
bitter = []
for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)
diff = float('inf')
for i in range(1, n + 1):
    for food in combinations(range(n), i):
        s = 1
        b = 0
        for j in food:
            s *= sour[j]
            b += bitter[j]
        diff = min(diff, abs(s - b))
print(diff)
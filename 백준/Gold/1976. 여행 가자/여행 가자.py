import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
parent = [i for i in range(n)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union(i, j)
plan = list(map(int, input().split()))
plan = [i- 1 for i in plan]
root = find(plan[0])
for city in plan:
    if find(city) != root:
        print('NO')
        break
else:
    print('YES')
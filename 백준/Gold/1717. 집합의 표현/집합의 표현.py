import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        parent[root2] = root1
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    cmd, a, b = map(int,input().split())
    if cmd == 0:
        union(a,b)
    elif cmd == 1:
        print('YES' if find(a) == find(b) else 'NO')
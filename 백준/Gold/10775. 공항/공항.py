import sys
input = sys.stdin.readline
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
plane = []
for _ in range(P):
    plane.append(int(input()))
count = 0
for p in plane:
    x = find_parent(p)
    if x == 0:
        break
    union_parent(x, x-1)
    count += 1
print(count)
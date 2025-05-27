import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
fee = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
for i in range(m):
    a, b = map(int,input().split())
    union(a, b)
for i in range(1, n+1):
    find(i)
friend = [0] * (n+1)
for i in range(1, n+1):
    temp = find(i)
    if friend[temp] == 0:
        friend[temp] = fee[temp]
    else:
        friend[temp] = min(friend[temp], fee[i])
answer = sum(friend)
if answer <= k:
    print(answer)
else:
    print('Oh no')
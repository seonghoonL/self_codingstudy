import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
count = [0] * (d + 1)
unique = 0
for i in range(k):
    if count[belt[i]] == 0:
        unique += 1
    count[belt[i]] += 1
max_kind = unique + (1 if count[c] == 0 else 0)
for i in range(1, N):
    left = belt[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    right = belt[(i + k - 1) % N]
    if count[right] == 0:
        unique += 1
    count[right] += 1
    current_kind = unique + (1 if count[c] == 0 else 0)
    if current_kind > max_kind:
        max_kind = current_kind
print(max_kind)
import sys
input = sys.stdin.readline
s, p = map(int, input().split())
dna = input().strip()
A, C, G, T = map(int, input().split())
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
check = {'A': A, 'C': C, 'G': G, 'T': T}
cnt = 0
for i in range(p):
    current[dna[i]] += 1
def is_valid():
    return all(current[x] >= check[x] for x in "ACGT")
if is_valid():
    cnt += 1
for i in range(p, s):
    current[dna[i]] += 1
    current[dna[i - p]] -= 1
    if is_valid():
        cnt += 1
print(cnt)
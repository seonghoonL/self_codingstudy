import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
dp = len(A) // 2
s = sum(A[:dp])
p = sum(A[dp:])
print(s, p)
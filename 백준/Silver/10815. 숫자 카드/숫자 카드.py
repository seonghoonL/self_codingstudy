import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

dic = {}

for o in card2:
    dic[o] = 0

for c in card:
    if c in dic:
        dic[c] = 1

for d in dic:
    print(dic[d], end=' ')
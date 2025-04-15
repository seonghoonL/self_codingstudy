import sys
input = sys.stdin.readline
w=[input().rstrip()for _ in range(5)]
re=''
for c in range(15):
    for r in range(5):
        if c<len(w[r]):
            re+=w[r][c]
print(re)
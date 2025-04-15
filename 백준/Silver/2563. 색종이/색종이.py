import sys
input = sys.stdin.readline
paper = [[0] * 100 for _ in range(100)]
n = int(input().strip())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
area = sum(sum(row) for row in paper)
print(area)
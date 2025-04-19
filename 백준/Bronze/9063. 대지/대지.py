n = int(input())
xc = []
yc = []
for _ in range(n):
    x, y = map(int, input().split())
    xc.append(x)
    yc.append(y)
width = max(xc) - min(xc)
height = max(yc) - min(yc)
print(width * height)
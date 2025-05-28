import sys
depth = 0
for line in sys.stdin:
    t, x = line.strip().split()
    x = int(x)
    if t == "Stair":
        depth += x * 17
    elif t == "Es":
        depth += x * 21
print(depth)
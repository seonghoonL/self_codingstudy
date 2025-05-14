N = int(input())
mirror = [input().strip() for _ in range(N)]
K = int(input())
if K == 1:
    for row in mirror:
        print(row)
elif K == 2:
    for row in mirror:
        print(row[::-1])
elif K == 3:
    for row in reversed(mirror):
        print(row)
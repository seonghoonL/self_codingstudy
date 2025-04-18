import sys
from collections import deque
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
balloons = deque((i + 1, num) for i, num in enumerate(nums))
result = []
while balloons:
    idx, move = balloons.popleft()
    result.append(idx)
    if not balloons:
        break
    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)
print(*result)
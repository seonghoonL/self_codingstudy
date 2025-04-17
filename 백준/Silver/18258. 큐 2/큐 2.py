import sys
from collections import deque
input = sys.stdin.readline
q = deque()
n = int(input())
for _ in range(n):
    cmd = input().strip()
    if cmd.startswith("push"):
        _, val = cmd.split()
        q.append(val)
    elif cmd == "pop":
        print(q.popleft() if q else -1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(0 if q else 1)
    elif cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "back":
        print(q[-1] if q else -1)
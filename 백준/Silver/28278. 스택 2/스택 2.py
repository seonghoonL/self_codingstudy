import sys
input = sys.stdin.readline
n = int(input().strip())
stack = []
for _ in range(n):
    data = list(map(int, input().strip().split()))
    if data[0] == 1:
        stack.append(data[1])
    elif data[0] == 2:
        print(stack.pop() if stack else -1)
    elif data[0] == 3:
        print(len(stack))
    elif data[0] == 4:
        print(1 if not stack else 0)
    elif data[0] == 5:
        print(stack[-1] if stack else -1)
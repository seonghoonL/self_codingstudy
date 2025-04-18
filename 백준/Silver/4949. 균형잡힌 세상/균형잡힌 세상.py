import sys
while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    stack = []
    balanced = True
    for char in line:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
    if balanced and not stack:
        print("yes")
    else:
        print("no")
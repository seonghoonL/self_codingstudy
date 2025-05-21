import sys
from collections import deque
input = sys.stdin.readline
s = input()
stack = deque()
count = 0
for c in s:
    stack.append(c)
    if len(stack) < 4:
        continue  
    if stack[-1] != 'k':
        continue   
    temp = ''
    for i in reversed(range(1, 4 + 1)):
        temp += stack[-i]  
    if temp == 'kick':
        count += 1
print(count)
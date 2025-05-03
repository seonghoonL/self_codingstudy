import sys
input = sys.stdin.readline
N = int(input())
liq = list(map(int, input().split()))
liq.sort()
left = 0
right = N - 1
min_diff = abs(liq[left] + liq[right])
answer = (liq[left], liq[right])
while left < right:
    total = liq[left] + liq[right]
    if abs(total) < min_diff:
        min_diff = abs(total)
        answer = (liq[left], liq[right])
    if total == 0:
        break
    elif total < 0:
        left += 1
    else:
        right -= 1
print(answer[0], answer[1])
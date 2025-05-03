import sys
input = sys.stdin.readline
N, C = map(int, input().split())
home = []
for _ in range(N):
    a = int(input())
    home.append(a)
home.sort()
def greedy(dist):
    count = 1
    last_position = home[0]
    for i in range(1, N):
        if home[i] - last_position >= dist:
            count+=1
            last_position = home[i]
    return count >= C
left = 1
right = home[-1] - home[0]
answer = 0
while left <= right:
    mid = (left + right) //2
    if greedy(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
n = int(input())
arr = list(map(int, input().split()))
count = [0] * 100001
left = 0
answer = 0
for right in range(n):
    count[arr[right]] += 1
    while count[arr[right]] > 1:
        count[arr[left]] -= 1
        left += 1
    answer += (right - left + 1)
print(answer)
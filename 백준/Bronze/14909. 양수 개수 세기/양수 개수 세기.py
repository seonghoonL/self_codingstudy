nums = map(int, input().split())
print(sum(1 for num in nums if num > 0))
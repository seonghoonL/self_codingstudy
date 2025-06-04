n = int(input())
codes = list(map(int, input().split()))
length = 0
for code in codes:
    length += 2 if code == 0 else 1 / code
print(length)
n = int(input())
if n % 2 == 0:
    sequence = [1, 2] * (n // 2)
else:
    sequence = [1, 2] * (n // 2) + [3]
print(*sequence)
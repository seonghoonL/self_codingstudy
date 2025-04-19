a, b, c = sorted(map(int, input().split()))
if a + b > c:
    print(a + b + c)
else: 
    print((a + b) * 2 - 1)

N, B = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""
while N > 0:
    res = digits[N % B] + res
    N //= B
print(res)
import math
A, B = map(int, input().split())
D = (2 * A) ** 2 - 4 * B
sqrt_D = int(math.isqrt(D))
x1 = (-2 * A + sqrt_D) // 2
x2 = (-2 * A - sqrt_D) // 2
roots = sorted({x1, x2})
print(*roots)
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
numbers = list(map(int, data[1:]))
MAX = 10**6
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False
primes = [i for i, val in enumerate(is_prime) if val]
for num in numbers:
    found = False
    for p in primes:
        if num % p == 0:
            found = True
            break
    print("NO" if found else "YES")
T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    count = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        time_needed = d / v
        fuel_needed = time_needed * c
        if fuel_needed <= f:
            count += 1
    print(count)
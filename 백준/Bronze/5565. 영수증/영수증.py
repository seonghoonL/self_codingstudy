total = int(input())
known_prices = [int(input()) for _ in range(9)]
print(total - sum(known_prices))
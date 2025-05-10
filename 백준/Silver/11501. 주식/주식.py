import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split())) 
    max_price = 0
    profit = 0
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price
    print(profit)
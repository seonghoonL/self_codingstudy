P = int(input())
change = 100 - P
quarters = change // 25
change %= 25
dimes = change // 10
change %= 10
nickels = change // 5
change %= 5
pennies = change
print(quarters, dimes, nickels, pennies)
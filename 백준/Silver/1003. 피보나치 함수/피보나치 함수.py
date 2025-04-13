import sys
input = sys.stdin.readline
T = int(input())
dp = [(0, 0)] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)
for i in range(2, 41):
    zero_count = dp[i-1][0] + dp[i-2][0]
    one_count = dp[i-1][1] + dp[i-2][1]
    dp[i] = (zero_count, one_count)
for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])
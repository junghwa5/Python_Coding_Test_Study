n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 1

if n == 1:
    print(dp[1])
else:
    dp[2] = 3
    if n == 2:
        print(dp[2])
    else:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + 2*dp[i-2]
        print(dp[i] % 10007)
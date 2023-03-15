n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 1

if n == 1:
    print(dp[1])
elif n == 2:
    dp[2] = 3
    print(dp[2])
else:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
        
    print(dp[i] % 10007)
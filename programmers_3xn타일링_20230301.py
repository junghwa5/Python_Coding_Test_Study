def solution(n):
    dp = [0 for i in range(n+1)]
    
    if n % 2:
        return 0
    elif n == 2:
        return 3
    elif n == 4:
        return 11
    else:
        dp[2] = 3
        dp[4] = 11
        for i in range(6, n+1, 2):
            dp[i] += (dp[i-2]*3 + 2)
            for j in range(2, i-3, 2):
                dp[i] += dp[j]*2
        return dp[n] % 1000000007

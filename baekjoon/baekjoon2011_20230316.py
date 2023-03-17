array = list(map(int,input()))
a_len = len(array)
dp = [0 for _ in range(a_len+1)]

if array[0] == 0:
    print(0)
else:
    array.insert(0, 0)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, a_len+1):
        if array[i] != 0:
            dp[i] += dp[i-1]
        tmp = array[i-1]*10 + array[i]
        if tmp >= 10 and tmp <= 26:
            dp[i] += dp[i-2]
    print(dp[a_len] % 1000000)
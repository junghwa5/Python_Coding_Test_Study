import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
array = [0] + array
dp = [0]*(n+1)
dp[1] = array[0]
for a in range(1, n+1):
    dp[a] = dp[a-1] + array[a]

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])
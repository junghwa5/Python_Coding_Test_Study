import sys
input = sys.stdin.readline

n = int(input())
t_list = []
p_list = []
for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

dp = [0]*(n+1) # 얻을 수 있는 최대 수익
for i in range(n-1, -1, -1):
    if t_list[i] + i > n: # 상담을 하면 퇴사일을 넘기게 되는 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + t_list[i]] + p_list[i])

print(dp[0])
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

start, end = 0, n-1 # 양끝부터 시작
n1, n2 = 0, 0
num = 2000000000
while start < end:
    temp = n_list[start] + n_list[end]
    if abs(temp) <= num: # 특성값이 0에 더 가까울 경우
        n1 = n_list[start]
        n2 = n_list[end]
        num = abs(temp)

    if temp < 0: # 특성값이 음수라면
        start += 1
    elif temp == 0: # 0이면 종료
        break
    else: # 특성값이 양수라면
        end -= 1
print(n1, n2)
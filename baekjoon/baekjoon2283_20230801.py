import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l_list = [0] * 1000001
max_num = 0 # 구간의 오른쪽 끝점 중 가장 큰 값
for _ in range(n):
    n1, n2 = map(int, input().split())
    if n2 > max_num:
        max_num = n2
    for i in range(n1, n2): # 구간 저장
        l_list[i] += 1

temp = 0
start, end = 0, 0
while True:
		# 시작점이 끝점보다 커지거나 끝점이 max값을 넘어서면
    if start > end or end > max_num:
        print(0, 0)
        break
    
    if temp == k: # 길이의 총합이 k와 같으면
        print(start, end)
        break
    elif temp < k: # 길이의 총합이 k보다 작으면
        temp += l_list[end]
        end += 1 # 끝점을 1 늘림
    else: # 길이의 총합이 k보다 크면
        temp -= l_list[start]
        start += 1 # 시작점을 1 늘림
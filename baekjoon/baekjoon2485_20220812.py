import math

# 입력 받기
n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))

# 원소 간의 차를 리스트 저장
n_li = []    
for j in range(n-1):
    n_li.append(n_list[j+1] - n_list[j])

# 최대공약수 구하기
g = n_li[0]
for k in range(1, len(n_li)):
    g = math.gcd(g, n_li[k]) # 유클리드 호제법

# 추가할 가로수 개수 구하기
num = (max(n_list) - min(n_list)) // g
print(num - len(n_list) + 1)
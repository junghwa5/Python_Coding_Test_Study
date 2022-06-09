import sys
input = sys.stdin.readline
import math

n, s = map(int, input().split())
a_list = list(map(int, input().split()))
gap_li = []

for i in range(n):
    if a_list[i] >= s:
        gap_li.append(a_list[i] - s)
    else:
        gap_li.append(s - a_list[i])
        
# print(math.gcd(gap_li)) # gcd() 안에 리스트를 넣으면 오류남
ss = gap_li[0]
for g in gap_li:
    ss = math.gcd(g, ss)

print(ss)
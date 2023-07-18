import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
alpha_list = input().split()
alpha_list.sort()

temp = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트
# L개의 조합
combi = list(combinations(alpha_list, l))

for co in combi:
    num = 0 # 모음의 개수
    for co2 in co:
        if co2 in temp:
            num += 1
    # 모음의 개수가 1개 이상이고 L-2(자음의 개수 최소 2개) 이하인 경우
    if num >= 1 and num <= l-2:
        s = ''.join(co)
        print(s)
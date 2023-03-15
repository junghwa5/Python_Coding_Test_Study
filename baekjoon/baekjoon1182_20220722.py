import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    comb = combinations(n_list, i)
    for c in comb:
        if sum(c) == s:
            cnt += 1
            
print(cnt)
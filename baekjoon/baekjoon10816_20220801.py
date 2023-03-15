import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
cnt = Counter(n_list)
m = int(input())
m_list = list(map(int, input().split()))

answer = []
for mm in m_list:
    answer.append(cnt[mm])
    
print(*answer)
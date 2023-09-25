import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

combi = list(combinations(list(range(n)), n//2)) # 조합
c_len = len(combi)
answer = int(1e9)
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] 에서 반 나눠서 진행
# combi[0]과 combi[-1]을 합하면 전체 팀원이 됨
for i in range(c_len // 2):
    start_team, link_team = 0, 0
    for a, b in list(combinations(combi[i], 2)):
        start_team += (graph[a][b] + graph[b][a])
    for c, d in list(combinations(combi[c_len-i-1], 2)):
        link_team += (graph[c][d] + graph[d][c])
    answer = min(answer, abs(start_team - link_team)) # 팀 능력치 차이 최소

print(answer)
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
        
def bfs(graph, root, visited):
    queue = deque([root])
    visited[root] = True # 시작 컴퓨터 방문
    cnt = 1

    while queue:
        n = queue.popleft()
        
        # 해킹 가능한 컴퓨터 탐색
        for c in graph[n]:
            if not visited[c]: # 방문하지 않은 컴퓨터
                queue.append(c)
                visited[c] = True
                cnt += 1
                
    return cnt

com_cnt = [0] # 해킹가능 컴퓨터 수
for i in range(1, n+1):
    visited = [False] * (n+1)
    com_cnt.append(bfs(graph, i, visited))   
        
max_cnt = max(com_cnt)
for i in range(1, n+1):
    if com_cnt[i] == max_cnt:
        print(i, end=' ')
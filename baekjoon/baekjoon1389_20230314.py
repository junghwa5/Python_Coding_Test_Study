import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = 1e9
graph = [[INF]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                
answer = sum(graph[0])
idx = 1
for i in range(1, n):
    if answer > sum(graph[i]):
        answer = sum(graph[i])
        idx = i+1
print(idx)
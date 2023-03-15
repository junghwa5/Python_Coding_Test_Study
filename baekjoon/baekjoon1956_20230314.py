import sys
input = sys.stdin.readline
v, e = map(int, input().split())
INF = 1e9
graph = [[INF]*v for _ in range(v)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    
for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = INF
for a in range(v):
    answer = min(answer, graph[a][a])
    
if answer == INF:
    print(-1)
else:
    print(answer)
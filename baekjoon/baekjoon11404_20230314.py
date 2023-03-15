import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
graph = [[INF]*n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                
for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
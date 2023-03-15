import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
                
cnt = 0
for i in range(n):
    s = 0
    for j in range(n):
        s += (graph[i][j] + graph[j][i])
    if s == n-1:
        cnt += 1
        
print(cnt)
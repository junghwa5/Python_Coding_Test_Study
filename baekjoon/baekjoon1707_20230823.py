import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    for edge in graph[v]:
        if visited[edge] == 0: # 연결된 정점이 색칠되어있지 않다면
            if visited[v] == 1:
                visited[edge] = 2
            elif visited[v] == 2:
                visited[edge] = 1
            temp = dfs(graph, edge, visited)
            if not temp:
                return False
        else:
            if visited[v] == visited[edge]:
                return False
    return True

k = int(input()) # 테스트케이스 개수
for _ in range(k):
    v, e = map(int, input().split()) # 정점 개수, 간선 개수
    visited = [0] * (v+1) # 정점 색칠
    graph = [[] for _ in range(v+1)] # 간선 정보

    for _ in range(e):
        u1, u2 = map(int, input().split())
        graph[u1].append(u2)
        graph[u2].append(u1)

    result = True
    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            if not dfs(graph, i, visited):
                result = False
                break
    
    if result:
        print("YES")
    else:
        print("NO")
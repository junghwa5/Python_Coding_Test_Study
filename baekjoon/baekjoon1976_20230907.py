import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    graph[i][i] = 1 # 출발과 도착이 같은 경우

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

plan = list(map(int, input().split()))
for i in range(m-1):
    if graph[plan[i] - 1][plan[i+1] - 1] == 0:
        print("NO")
        break
else:
    print("YES")
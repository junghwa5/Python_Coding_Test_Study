import sys, heapq
input = sys.stdin.readline
INF = 1e9
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
        
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(queue, (dist+i[1], i[0]))

dijkstra(x)
answer = []
for j in range(1, n+1):
    if k == distance[j]:
        print(j)
        answer.append(j)
if len(answer) == 0:
    print(-1)
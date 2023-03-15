import sys, heapq
input = sys.stdin.readline
INF = 1e9
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())
cost = [INF] * (n+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    cost[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        if cost[now] < dist:
            continue
        for j in graph[now]:
            if dist+j[1] < cost[j[0]]:
                cost[j[0]] = dist+j[1]
                heapq.heappush(queue, (dist+j[1], j[0]))
                
dijkstra(s)
print(cost[e])
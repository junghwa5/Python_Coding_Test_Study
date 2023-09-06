from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] == 1:
            queue.append([i, j]) # 상어 위치를 queue에 저장
cnt = 0

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                queue.append([ny, nx])
                graph[ny][nx] = graph[y][x] + 1 # 거리 정보 업데이트

bfs()
print(max(map(max, graph)) - 1) # graph에서 가장 큰 값 - 1
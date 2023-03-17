import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                cnt = max(cnt, visited[nx][ny])
    return cnt-1

dist = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            dist = max(dist, bfs(i, j))
            
print(dist)
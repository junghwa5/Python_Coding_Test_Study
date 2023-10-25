import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: # 목표지점
            queue.append([i, j])
            visited[i][j] = 0
        if graph[i][j] == 0: # 갈 수 없는 땅
            visited[i][j] = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# bfs
while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        # 방문한 적 없고 갈 수 있다면
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and visited[ny][nx] == -1:
            queue.append([ny, nx])
            visited[ny][nx] = visited[y][x] + 1

for i in range(n):
    print(*visited[i])
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    temp = list(input())
    graph.append(temp)
    for j in range(m):
        if temp[j] == 'I':
            start = [i, j]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[False]*m for _ in range(n)]
cnt = 0

queue = deque([start])
visited[start[0]][start[1]] = True
while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 'X' and visited[ny][nx] == False:
                queue.append([ny, nx])
                visited[ny][nx] = True

                if graph[ny][nx] == 'P':
                    cnt += 1

if cnt == 0:
    print("TT")
else:
    print(cnt)
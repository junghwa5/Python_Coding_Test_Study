from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1: # 범위를 벗어난 경우
                continue

            if graph[nx][ny] == 1: # 집이 있다면
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    
    return cnt

house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append(bfs(graph, i, j))

house.sort()
print(len(house))
for h in house:
    print(h)
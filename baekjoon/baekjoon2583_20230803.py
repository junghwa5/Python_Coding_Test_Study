import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2): # 직사각형 내부를 1로 변환
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(i, j): # bfs
    queue = deque()
    queue.append([i, j])
    d_list = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in d_list:
            ny = y + dy
            nx = x + dx
            # 모눈종이 안에 있고 분리된 부분에 속하는 경우
            if (0 <= ny < m) and (0 <= nx < n) and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append([ny, nx])
                cnt += 1
    return cnt

cnt_list = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            cnt_list.append(bfs(i, j))
print(len(cnt_list)) # 영역의 개수
print(*sorted(cnt_list)) # 각 영역의 넓이 오름차순 정렬
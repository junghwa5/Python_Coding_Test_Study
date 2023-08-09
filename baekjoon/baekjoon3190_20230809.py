import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 보드의 크기
graph = [([0]*n) for _ in range(n)] # 뱀이 이동할 보드

k = int(input()) # 사과의 개수
for _ in range(k):
    a_row, a_col = map(int, input().split()) # 사과의 위치(행, 열)
    graph[a_row-1][a_col-1] = 1
    
# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
direct_idx = 1
turn_list = deque([])
l = int(input())
for _ in range(l):
    x, c = input().split() # 뱀의 방향 변환 정보
    turn_list.append([int(x), c])
    
answer = 0
y, x = 0, 0
queue = deque([])
queue.append([0, 0])
while True:
    answer += 1
    ny = y + dy[direct_idx]
    nx = x + dx[direct_idx]
    
    if turn_list and answer == turn_list[0][0]:
        if turn_list[0][1] == 'L' and direct_idx == 0:
            direct_idx = 3
        elif turn_list[0][1] == 'L' and direct_idx > 0:
            direct_idx -= 1
        elif turn_list[0][1] == 'D' and direct_idx == 3:
            direct_idx = 0
        elif turn_list[0][1] == 'D' and direct_idx < 3:
            direct_idx += 1
        turn_list.popleft()
    
    if ny < 0 or ny >= n or nx < 0 or nx >= n or [ny, nx] in queue:
        break
    if graph[ny][nx] == 1: # 사과
        graph[ny][nx] = 0
        y = ny
        x = nx
        queue.append([y, x])
    else:
        y = ny
        x = nx
        queue.popleft() # 꼬리 위치 비움
        queue.append([y, x])
                
print(answer)
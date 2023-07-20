import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# 방향 리스트(북, 동, 남, 서)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph[r][c] = 2
answer = 1 # 첫 시작 방문
while True:
    for _ in range(4):
        d -= 1 # 반시계방향으로 90도 회전
        if d == -1:
            d = 3
        nr = r + dr[d]
        nc = c + dc[d]
        
        if graph[nr][nc] == 0:
            graph[nr][nc] = 2 # 방문하면 2로 표시
            answer += 1
            r = nr
            c = nc
            break
    else: # 청소되지 않은 빈 칸이 없는 경우
        nr = r - dr[d]
        nc = c - dc[d]
        
        if graph[nr][nc] == 1: # 뒤가 벽인 경우
            print(answer)
            break
        else:
            r = nr
            c = nc
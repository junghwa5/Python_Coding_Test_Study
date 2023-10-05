import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
cctv = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] in [1,2,3,4,5]:
            cctv.append([temp[j], i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
direction = {
    1: [[0], [1], [2], [3]], 
    2: [[0, 2], [1, 3]], 
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

answer = n*m
def dfs(i, graph):
    global answer
    temp = copy.deepcopy(graph)

    if i == len(cctv):
        cnt = 0
        for t in temp:
            cnt += t.count(0)
        answer = min(answer, cnt)
        return

    num, y, x = cctv[i]
    for d in direction[num]:
        for idx in d:
            ny = y
            nx = x
            while True:
                ny += dy[idx]
                nx += dx[idx]
                if nx < 0 or ny < 0 or nx >= m or ny >= n or temp[ny][nx] == 6:
                    break
                elif temp[ny][nx] == 0:
                    temp[ny][nx] = 7
        dfs(i+1, temp)
        temp = copy.deepcopy(graph)

dfs(0, graph)
print(answer)
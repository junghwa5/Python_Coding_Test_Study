import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h + x)]

a = [b[i][:w] for i in range(h)] # 배열 a 초기화
for i in range(x, h):
    for j in range(y, w):
        a[i][j] = b[i][j] - a[i-x][j-y] # 겹치는 부분

for i in range(h):
    print(* a[i])
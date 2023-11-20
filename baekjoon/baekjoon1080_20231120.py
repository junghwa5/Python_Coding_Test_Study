import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
b = [list(map(int, list(input().rstrip()))) for _ in range(n)]

answer = 0
if (n < 3 or m < 3) and a != b:
    answer = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                answer += 1
                for y in range(i, i+3):
                    for x in range(j, j+3):
                        if a[y][x] == 0:
                            a[y][x] = 1
                        else:
                            a[y][x] = 0

if a != b:
    answer = -1
print(answer)
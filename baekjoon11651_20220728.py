import sys
input = sys.stdin.readline
n = int(input())
co = []
for _ in range(n):
    co.append(list(map(int, input().split())))
    
co.sort(key=lambda x: (x[1], x[0]))
for c in co:
    print(*c)
import sys
input = sys.stdin.readline

N = int(input())
fac = 1
cnt = 0

for i in range(N, 0, -1):
    fac *= i
    
for s in str(fac)[::-1]:
    if s != '0':
        break
    else:
        cnt += 1

print(cnt)
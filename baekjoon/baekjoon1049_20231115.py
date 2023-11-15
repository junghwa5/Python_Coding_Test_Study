import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p1 = [] # 패키지 가격
p2 = [] # 낱개 가격
for _ in range(m):
    a, b = map(int, input().split())
    p1.append(a)
    p2.append(b)
p1.sort()
p2.sort()

if p1[0] < p2[0] * 6:
    num1 = n // 6
    num2 = n % 6
    if p1[0] <= num2 * p2[0]:
        answer = (num1 + 1) * p1[0]
    else:
        answer = num1 * p1[0] + num2 * p2[0]
else:
    answer = n * p2[0]
print(answer)
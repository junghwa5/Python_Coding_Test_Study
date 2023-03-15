import math

def lcm(x, y):  # 최소공배수 구하기
    return (x*y) // math.gcd(x,y)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
from collections import defaultdict
import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())
a = defaultdict(int) # int형 딕셔너리 생성
a[0] = 1

def func(n):
    if n in a: # n번째 값이 딕셔너리에 있다면
        return a[n]
    else: # n번째 값이 딕셔너리에 없다면
        a[n] = func(n//p) + func(n//q)
        return a[n]

print(func(n))
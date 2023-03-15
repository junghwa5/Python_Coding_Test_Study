import sys
input = sys.stdin.readline
import math

t = int(input())

for _ in range(t):
    test_case = list(map(int, input().split()))
    n = test_case[0]
    result = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            result += math.gcd(test_case[i], test_case[j])
    print(result)
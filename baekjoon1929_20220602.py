import math
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

def is_prime_num(n): # 에라토스테네스의 체
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr

arr = is_prime_num(n)

for i in range(m, n+1):
    if arr[i]:
        print(i)
import sys
input = sys.stdin.readline
import math

T = int(input())
nums = [int(input()) for _ in range(T)]

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

max_num = max(nums)
arr = is_prime_num(max_num)

for num in nums:
    cnt = 0
    
    for a in range(2, (num//2) + 1):
        if arr[a] and arr[num - a]:
            cnt += 1
    print(cnt)
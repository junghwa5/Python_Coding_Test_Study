import math
import sys

input = sys.stdin.readline

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

num = -1
arr = is_prime_num(1000000)

while num != 0:
    num = int(input())
    
    for a in range(3, len(arr)):
        if arr[a] and arr[num - a]:
            print("{0} = {1} + {2}".format(num, a, num-a))
            break
#     else:
#         print("Goldbach's conjecture is wrong.")
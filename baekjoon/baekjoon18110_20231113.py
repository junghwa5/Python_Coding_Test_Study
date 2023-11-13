import sys
input = sys.stdin.readline

n = int(input().strip())

def func(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if n == 0:
    print(0)
else:
    n_list = [int(input().strip()) for _ in range(n)]
    n_list.sort()
    num = func(n * 0.15)
    
    if num == 0:
        print(func(sum(n_list) / n))
    else:
        print(func(sum(n_list[num:-num]) / (n - 2*num)))
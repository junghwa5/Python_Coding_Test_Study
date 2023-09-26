import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
o1, o2, o3, o4 = map(int, input().split()) # 연산자의 개수
o_list = ['+']*o1 + ['-']*o2 + ['*']*o3 + ['//']*o4

perm = list(set(list(permutations(o_list, n-1)))) # 순열
max_num = int(-1e9)
min_num = int(1e9)
for p in perm:
    temp = n_list[0]
    for i in range(1, n):
        if p[i-1] == '+':
            temp += n_list[i]
        elif p[i-1] == '-':
            temp -= n_list[i]
        elif p[i-1] == '*':
            temp *= n_list[i]
        elif p[i-1] == '//':
            if temp < 0:
                temp = -(abs(temp) // n_list[i])
            else:
                temp //= n_list[i]

    max_num = max(max_num, temp)
    min_num = min(min_num, temp)

print(max_num)
print(min_num)
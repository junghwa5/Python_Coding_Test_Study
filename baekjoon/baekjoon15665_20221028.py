from itertools import product

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
li = []
for _ in range(m):
    li.append(n_list)

answer = list(set(product(*li)))
answer.sort()
for a in answer:
    print(*a)
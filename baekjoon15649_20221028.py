from itertools import permutations

n, m = map(int, input().split())
n_list = [i for i in range(1, n+1)]

answer = list(permutations(n_list, m))
for a in answer:
    print(*a)
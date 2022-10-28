from itertools import combinations

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

answer = list(set(combinations(n_list, m)))
answer.sort()
for a in answer:
    print(*a)
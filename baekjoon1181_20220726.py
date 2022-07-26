import sys
input = sys.stdin.readline

n = int(input())

alpha_li = []
for _ in range(n):
    alpha_li.append(input().rstrip())

alpha_set = set(alpha_li)
alpha_li = list(alpha_set)
alpha_li.sort()
alpha_li.sort(key=lambda x: len(x))

for alpha in alpha_li:
    print(alpha)
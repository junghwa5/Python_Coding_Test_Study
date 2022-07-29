import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list = list(set(n_list))
n_list.sort()

print(*n_list)
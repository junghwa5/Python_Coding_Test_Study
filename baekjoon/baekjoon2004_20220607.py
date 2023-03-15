import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def num_count(n, k):
    cnt = 0
    while n:
        n = n // k
        cnt += n
    return cnt


five_cnt = num_count(n, 5) - num_count(m, 5) - num_count(n - m, 5)
two_cnt = num_count(n, 2) - num_count(m, 2) - num_count(n - m, 2)

print(min(five_cnt, two_cnt))
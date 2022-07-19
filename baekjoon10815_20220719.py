import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(n_list, value): # 이진탐색 함수
    start, end = 0, n-1

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == value:
            return 1
        elif n_list[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
            
    return 0

for mm in m_list:
    print(binary_search(n_list, mm), end = ' ')
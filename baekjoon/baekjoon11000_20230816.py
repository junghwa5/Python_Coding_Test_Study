import sys, heapq
input = sys.stdin.readline

n = int(input())
# [시작시간, 종료시간]
li = [list(map(int, input().split())) for _ in range(n)]
li.sort()

hq = []
heapq.heappush(hq, li[0][1])
for i in range(1, n):
    if li[i][0] < hq[0]: # 강의 시작시간이 hq(우선순위큐) 첫번째 값보다 작다면
        heapq.heappush(hq, li[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, li[i][1])

print(len(hq))
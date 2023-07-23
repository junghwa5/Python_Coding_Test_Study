import sys
input = sys.stdin.readline
import heapq

n = int(input())
problem = [] 
for _ in range(1, n+1):
    problem.append(list(map(int, input().split())))
problem.sort(key = lambda x:(x[0], -x[1])) # 데드라인 - 오름차순, 컵라면 수 - 내림차순

heap = []
for p in problem:
    if len(heap) < p[0]: # 현재 데드라인이 푼 문제 수보다 클 경우
        heapq.heappush(heap, p[1])
    else:
        if p[1] > heap[0]: # 현재 문제를 푸는 것이 이득이라면
            heapq.heappop(heap)
            heapq.heappush(heap, p[1])
            
print(sum(heap))
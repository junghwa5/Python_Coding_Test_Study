import sys, heapq

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
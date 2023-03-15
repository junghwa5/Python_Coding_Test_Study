import sys

n = int(sys.stdin.readline())
qu = [int(sys.stdin.readline()) for i in range(n)] # 큐에 입력한 것 저장

res = 0
for b in range(len(qu)):
    b_queue = qu # 큐 복사
    num = b_queue.pop(0) # 작은 빌딩번호의 높이 제거
    while b_queue and num <= b_queue[b]:
        res += 1

print(res)
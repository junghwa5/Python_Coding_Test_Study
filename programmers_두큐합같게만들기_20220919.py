from collections import deque

def solution(queue1, queue2):
    answer = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    dq1_sum = sum(dq1)
    dq2_sum = sum(dq2)
    total_sum = dq1_sum + dq2_sum
    
    # 두 큐의 원소 합이 홀수인 경우
    if (total_sum % 2) == 1:
        return -1
    # 큐의 원소 최대값이 전체 합의 1/2보다 큰 경우
    if (total_sum/2) < max(dq1) or (total_sum/2) < max(dq2):
        return -1
    
    while dq1_sum != dq2_sum:
        if dq1_sum > dq2_sum:
            num = dq1.popleft()
            dq2.append(num)
            answer += 1
            dq1_sum -= num
            dq2_sum += num
        else:
            num = dq2.popleft()
            dq1.append(num)
            answer += 1
            dq1_sum += num
            dq2_sum -= num
        
        if answer == len(queue1)*3:
            answer = -1
            break
    
    return answer
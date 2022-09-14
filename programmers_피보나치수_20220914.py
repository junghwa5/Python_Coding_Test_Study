def solution(n):
    answer = [0, 1]
    for i in range(2, n+1):
        num = answer[i-2] + answer[i-1]
        if num < 1234567:
            answer.append(num)
        else:
            answer.append(num % 1234567)
    return answer[-1]
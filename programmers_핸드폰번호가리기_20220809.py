def solution(phone_number):
    answer = ''
    leng = len(phone_number)
    for _ in range(leng - 4):
        answer += '*'
    answer += phone_number[-4:]
    
    return answer
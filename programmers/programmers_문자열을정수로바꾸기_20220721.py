def solution(s):
    answer = 0
    
    if s[0] == '-1':
        answer = int(s[1:])
        answer *= -1
    else:
        answer = int(s)
    
    return answer
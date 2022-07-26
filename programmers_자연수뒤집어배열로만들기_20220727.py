def solution(n):
    answer = []
    str_n = str(n)
    rev_n = str_n[::-1]
    
    for s in rev_n:
        s = int(s)
        answer.append(s)
        
    return answer
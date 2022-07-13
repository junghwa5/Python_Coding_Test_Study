def sum_gauss(n): # 1부터 n까지의 합
    return int(n*(n+1)/2)

def solution(a, b):
    answer = 0
    
    if a >= b:
        answer = sum_gauss(a) - sum_gauss(b-1)
    else:
        answer = sum_gauss(b) - sum_gauss(a-1)
    
    return answer
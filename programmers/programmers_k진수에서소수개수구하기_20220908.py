def convert(num, k): # 10진수를 k진수로 변경
    tmp = "0123456789ABCDEF"
    q, r = divmod(num, k)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, k) + tmp[r]

def primenumber(x): # 소수 판별
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    k_num = convert(n, k) # k진수로 변경
    p_list = k_num.split('0') # 0을 기준으로 나누어 리스트 저장
    for p in p_list: # 소수 개수 구함
        if p != '' and primenumber(int(p)):
            answer += 1
    
    return answer

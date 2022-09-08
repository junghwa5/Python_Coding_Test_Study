def convert(num, k):
    tmp = "0123456789ABCDEF"
    q, r = divmod(num, k)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, k) + tmp[r]

def primenumber(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    k_num = convert(n, k)
    p_list = k_num.split('0')
    for p in p_list:
        if p != '' and primenumber(int(p)):
            answer += 1
    
    return answer
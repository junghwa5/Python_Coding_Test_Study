def solution(a, b):
    answer = ''
    w_li = ['THU', 'FRI','SAT','SUN','MON','TUE','WED']
    m_li = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    num = 0
    for i in range(a-1):
        num += m_li[i]
    num += b
    num %= 7
    answer = w_li[num]
    
    return answer
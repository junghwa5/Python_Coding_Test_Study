from collections import Counter

def solution(N, stages):
    answer = []
    c_dic = {}
    cnt = Counter(stages)
    leng = len(stages)
    
    for n in range(1, N+1):
        num1 = cnt[n]
        num2 = leng
        for i in range(1, n):
            num2 -= cnt[i]
        if num1 == 0 or num2 == 0:
            c_dic[n] = 0
        else:
            c_dic[n] = num1/num2

    answer = sorted(c_dic, key=c_dic.get, reverse=True)
    
    return answer
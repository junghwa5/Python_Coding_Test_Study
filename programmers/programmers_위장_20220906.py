def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes: # 딕셔너리를 이용하여 의상의 종류별 이름 분류
        if c[1] in dic:
            dic.get(c[1]).append(c[0])
        else:
            dic[c[1]] = [c[0]]
        
    key_list = list(dic.keys())
    for k in key_list: # 의상의 종류별 개수 + 1을 곱함
        num = len(dic.get(k)) + 1
        answer *= num
    answer -= 1 # 모든 의상을 입지 않는 경우를 뺌
        
    return answer
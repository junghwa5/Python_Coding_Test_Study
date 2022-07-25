def solution(s):
    answer = ''
    
    s_list = s.split(" ")
    
    for ss in s_list:
        for i in range(len(ss)):
            if i % 2 == 0:
                answer += ss[i].upper()
            else:
                answer += ss[i].lower()
        answer += " "
    
    return answer[:-1]
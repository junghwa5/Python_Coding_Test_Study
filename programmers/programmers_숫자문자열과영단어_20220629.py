def solution(s):
    answer = ""
    al_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
              'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    temp_li = []
    
    for st in s:
        if st.isalpha():
            temp_li.append(st)
            string = ''.join(temp_li)
            if string in al_dic:
                answer += al_dic[string]
                temp_li = []
        elif st.isdigit():
            answer += st
    
    return int(answer)
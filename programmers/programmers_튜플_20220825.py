def solution(s):
    answer = []
    
    s_list = s.replace("{", "").replace("}}", "").split("},")
    s_list.sort(key=len)
    
    for st in s_list:
        st_li = list(map(int, st.split(',')))
        for num in st_li:
            if num not in answer:
                answer.append(num)
    
    return answer
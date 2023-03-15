def solution(record):
    answer = []
    name_dict = {}
    chat = []
    
    for r in record:
        r_li = r.split()
        if r_li[0] == "Enter":
            name_dict[r_li[1]] = r_li[2]
            chat.append([r_li[0], r_li[1]])
        elif r_li[0] == "Leave":
            chat.append([r_li[0], r_li[1]])
        else:
            name_dict[r_li[1]] = r_li[2]
    
    for c in chat:
        if c[0] == "Enter":
            mes = name_dict[c[1]] + "님이 들어왔습니다."
            answer.append(mes)
        else:
            mes = name_dict[c[1]] + "님이 나갔습니다."
            answer.append(mes)
    
    return answer
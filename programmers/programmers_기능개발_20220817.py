def solution(progresses, speeds):
    answer = []
    day_list = []
    
    for p, s in zip(progresses, speeds):
        if (100 - p)%s == 0:
            day_list.append((100 - p)//s)
        else:
            day_list.append((100 - p)//s + 1)
    
    num = 1
    lar = day_list[0]
    for n in range(1, len(day_list)):
        if lar >= day_list[n]:
            if n == (len(day_list)-1):
                answer.append(num+1)
            else:
                num += 1
        else:
            if n == (len(day_list)-1):
                lar = day_list[n]
                answer.append(num)
                answer.append(1)
            else:
                lar = day_list[n]
                answer.append(num)
                num = 1
    
    return answer
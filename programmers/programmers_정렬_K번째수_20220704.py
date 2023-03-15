def solution(array, commands):
    answer = []
    
    for com in commands:
        temp = array[com[0]-1 : com[1]]
        temp = sorted(temp)
        num = temp[com[2]-1]
        answer.append(num)
    
    return answer
def solution(answers):
    # 1,2,3번의 수포자가 찍는 방식
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    # 맞출 경우 score 리스트의 값을 1 더함
    for i in range(len(answers)):
        if stu1[i%5] == answers[i]:
            score[0] += 1
        if stu2[i%8] == answers[i]:
            score[1] += 1
        if stu3[i%10] == answers[i]:
            score[2] += 1
    
    # 가장 많이 맞춘 사람을 result 리스트에 추가
    highest = max(score)
    result = [j+1 for j in range(3) if score[j] == highest]
    
    return result
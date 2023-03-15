def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    left_n = dic['*']
    right_n = dic['#']
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_n = dic[num]
        elif num in [3,6,9]:
            answer += 'R'
            right_n = dic[num]
        else:
            dist_l = abs(dic[num][0] - left_n[0]) + abs(dic[num][1] - left_n[1])
            dist_r = abs(dic[num][0] - right_n[0]) + abs(dic[num][1] - right_n[1])
            
            if dist_l < dist_r:
                answer += 'L'
                left_n = dic[num]
            elif dist_l > dist_r:
                answer += 'R'
                right_n = dic[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_n = dic[num]
                else:
                    answer += 'R'
                    right_n = dic[num]
    
    return answer
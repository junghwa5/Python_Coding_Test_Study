def solution(numbers):
    answer = ''
    s_numbers = []
    for n in numbers:
        s_numbers.append(str(n))
    s_numbers.sort(reverse = True)
    
    for s in s_numbers:
        answer += s
    
    if int(answer) == 0:
        answer = '0'
    
    return answer
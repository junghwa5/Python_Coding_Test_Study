def divisor(n): # n이 되는 2개의 자연수 조합 구하기
    divisor_list = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor_list.append([i, n//i])
    
    return divisor_list

def solution(brown, yellow):
    answer = []
    divisor_list = divisor(yellow)
    for y1, y2 in divisor_list:
        if (y1 + y2 + 2) * 2 == brown: # (가로 + 세로 + 2) * 2가 brown과 같으면
            answer.append(y1 + 2)
            answer.append(y2 + 2)
            answer.sort(reverse = True)
    
    return answer
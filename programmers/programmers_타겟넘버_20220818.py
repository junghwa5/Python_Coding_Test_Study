from itertools import product

def solution(numbers, target):
    answer = 0
    num_list = []
    for n in numbers:
        li = [n, -n]
        num_list.append(li)
    comb = list(product(*num_list))
    
    for c in comb:
        if sum(c) == target:
            answer += 1
    
    return answer
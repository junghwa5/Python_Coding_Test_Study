def solution(n, lost, reserve):
    answer = n
    
    new_lost = [l for l in lost if l not in reserve]
    new_lost.sort()
    new_reserve = [l for l in reserve if l not in lost]
    new_reserve.sort()
    
    for l in new_lost:
        if l-1 in new_reserve:
            new_reserve.remove(l-1)
        elif l+1 in new_reserve:
            new_reserve.remove(l+1)
        else:
            answer -= 1
    
    return answer
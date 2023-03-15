def solution(priorities, location):
    answer = 0
    loc = list(range(len(priorities)))
    arr = priorities.copy()
    
    while True:
        m = max(arr)
        if arr[0] == m:
            num = loc.pop(0)
            arr.pop(0)
            answer += 1
            if num == location:
                break
        else:
            loc.append(loc.pop(0))
            arr.append(arr.pop(0))
    
    return answer
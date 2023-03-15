def solution(x):
    num = []
    
    for i in str(x):
        num.append(int(i))
    
    return x % sum(num) == 0
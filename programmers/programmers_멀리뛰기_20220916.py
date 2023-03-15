def solution(n):
    if n < 3:
        return n
    
    fibo = [1,2]
    for i in range(2, n):
        fibo.append(fibo[i-2] + fibo[i-1])
        
    return fibo[-1] % 1234567
def solution(n):
    answer = ""
    str_n = str(n)
    n_li = list(str_n)
    n_li.sort(reverse=True)
    answer = ''.join(r for r in n_li)
    
    return int(answer)
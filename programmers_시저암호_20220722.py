def solution(s, n):
    answer = ''
    
    for ss in s:
        if ss.isupper():
            o = ord(ss) + n
            if o > ord('Z'):
                o -= 26
            answer += chr(o)
        elif ss.islower():
            o = ord(ss) + n
            if o > ord('z'):
                o -= 26
            answer += chr(o)
        else:
            answer += ss
        
    return answer
def iscorrect(s): # 올바른 문자열인지 확인
    stack = []
    
    for ps in s:
        if ps == '(':
            stack.append(ps)
        elif ps == ')':
            if stack:
                stack.pop()
            else:
                return False
    else:
        if len(stack) != 0:
            return False
        else:
            return True

def divide(s): # 균형잡힌 괄호 문자열 분리
    op = 0
    cl = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            op += 1
        elif s[i] == ')':
            cl += 1
            
        if op == cl:
            return s[:i+1], s[i+1:]
        
def solution(p):
    answer = ''
    
    # 1
    if len(p) == 0 or iscorrect(p):
        return p
    # 2
    u, v = divide(p)
    # 3
    if iscorrect(u):
        answer += u + solution(v)
    # 4
    else:
        # 4-1, 4-2. 4-3
        answer = '(' + solution(v) + ')'
        # 4-4
        for uu in u[1:-1]:
            if uu == '(':
                answer += ')'
            elif uu == ')':
                answer += '('
    # 4-5
    return answer
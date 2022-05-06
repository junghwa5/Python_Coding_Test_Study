import sys

n = int(input())

for i in range(n):
    ps_list = sys.stdin.readline()
    stack = [] # 스택 생성
    
    for ps in ps_list:
        if ps == '(':
            stack.append(ps)
        elif ps == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: # for문이 중간에 break되지 않은 경우
        if len(stack) != 0: # 스택이 비어있지 않으면
            print("NO")
        else: # 스택이 비어있으면
            print("YES")
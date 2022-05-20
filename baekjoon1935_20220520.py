n = int(input())

p_exp = input()
num_list = []
stack = []

for _ in range(n):
    num = int(input())
    num_list.append(num)
    
for p in p_exp:
    if p.isalpha(): # 알파벳일 경우
        stack.append(num_list[ord(p) - ord('A')])
    else: # 연산자일 경우
        num2 = stack.pop()
        num1 = stack.pop()
        if p == '+':
            stack.append(num1+num2)
        elif p == '-':
            stack.append(num1-num2)
        elif p == '*':
            stack.append(num1*num2)
        elif p == '/':
            stack.append(num1/num2)
            
print("{:.2f}".format(stack[0]))
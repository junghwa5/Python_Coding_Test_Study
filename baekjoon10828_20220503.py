import sys

n = int(sys.stdin.readline())

stack = []
for d in range(n):
    input_d = sys.stdin.readline().split()
    if input_d[0] == "push":
        stack.append(input_d[1])
    elif input_d[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif input_d[0] == "size":
        print(len(stack))
    elif input_d[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif input_d[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
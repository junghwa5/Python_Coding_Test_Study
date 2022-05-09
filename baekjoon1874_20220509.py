import sys

n = int(input())
stack = []
cnt = 1
answer = []

for i in range(n):
    num = int(sys.stdin.readline())
    # num까지 스택에 넣음
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    # num과 스택 맨 위의 수가 같으면
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    # for문 종료
    else:
        print("NO")
        break
else: # for문에서 한번도 break 되지 않았다면
    for i in answer:
        print(i)
import sys
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    p_num = [sys.stdin.readline().strip() for _ in range(num)]
    p_num.sort()
    
    for i in range(num-1):
        if p_num[i] == p_num[i+1][:len(p_num[i])]:
            print("NO")
            break
    else:
        print("YES")
import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

num = n
for a in a_list:
    a -= b
    
    if a > 0:
        if a % c == 0:
            num += a // c
        else:
            num += (a // c) + 1
            
print(num)
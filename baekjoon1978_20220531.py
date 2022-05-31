import sys

n = int(sys.stdin.readline()())
num_list = list(map(int, sys.stdin.readline().split(' ')))
result = 0

for num in num_list:
    if num == 1:
        continue
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        result += 1
        
print(result)
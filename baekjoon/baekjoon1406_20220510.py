import sys

str_li = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
r_li = []

for i in range(n):
    line = sys.stdin.readline().strip().split()
    if line[0] == 'L':
        if len(str_li) == 0:
            continue
        t = str_li.pop()
        r_li.append(t)
    elif line[0] == 'D':
        if len(r_li) == 0:
            continue
        t = r_li.pop()
        str_li.append(t)
    elif line[0] == 'B':
        if len(str_li) == 0:
            continue
        str_li.pop()
    elif line[0] == 'P':
        str_li.append(line[1])
        
result1 = ''.join(s for s in str_li)
r_li.reverse()
result2 = ''.join(r for r in r_li)
print(result1 + result2)